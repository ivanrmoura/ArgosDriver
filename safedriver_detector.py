"""
ArgosDriver AI: Sentinela Veicular Anti-Fadiga e Distração
Script em Python utilizando OpenCV e MediaPipe Face Mesh.
Mede EAR (Eye Aspect Ratio) para fechamento dos olhos e MAR (Mouth Aspect Ratio) para bocejos.
"""

import cv2
import math
import os
import time

try:
    import mediapipe as mp
    import numpy as np
except ImportError:
    print("Instale as dependências: pip install opencv-python mediapipe numpy")
    exit(1)

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

def dist_2d(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def calculate_ear(landmarks, w, h):
    # Olho Esquerdo
    dV_l = dist_2d((landmarks[159].x * w, landmarks[159].y * h), (landmarks[145].x * w, landmarks[145].y * h))
    dH_l = dist_2d((landmarks[33].x * w, landmarks[33].y * h), (landmarks[133].x * w, landmarks[133].y * h))
    ear_left = dV_l / (dH_l or 1)

    # Olho Direito
    dV_r = dist_2d((landmarks[386].x * w, landmarks[386].y * h), (landmarks[374].x * w, landmarks[374].y * h))
    dH_r = dist_2d((landmarks[362].x * w, landmarks[362].y * h), (landmarks[263].x * w, landmarks[263].y * h))
    ear_right = dV_r / (dH_r or 1)

    return (ear_left + ear_right) / 2

def calculate_mar(landmarks, w, h):
    # Lábios
    dV_m = dist_2d((landmarks[13].x * w, landmarks[13].y * h), (landmarks[14].x * w, landmarks[14].y * h))
    dH_m = dist_2d((landmarks[78].x * w, landmarks[78].y * h), (landmarks[308].x * w, landmarks[308].y * h))
    return dV_m / (dH_m or 1)

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    closed_frames = 0
    yawn_frames = 0
    total_yawns = 0

    # Carregar logomarca do ArgosDriver (se disponível)
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    logo_rgba = None
    if os.path.exists(logo_path):
        logo_img = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
        if logo_img is not None and logo_img.shape[2] == 4:
            target_h = 42
            target_w = int(logo_img.shape[1] * (target_h / logo_img.shape[0]))
            logo_rgba = cv2.resize(logo_img, (target_w, target_h), interpolation=cv2.INTER_AREA)

    print("=" * 60)
    print("🚗 ArgosDriver AI: Sentinela de Trânsito em Python")
    print("Pressione 'Q' para sair.")
    print("=" * 60)

    with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as face_mesh:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)

            status_text = "CONDUTOR FOCADO"
            status_color = (0, 223, 114) # Verde

            if results.multi_face_landmarks:
                lm = results.multi_face_landmarks[0].landmark

                ear = calculate_ear(lm, w, h)
                mar = calculate_mar(lm, w, h)

                # Rotação da Cabeça (Yaw)
                nose_x = lm[1].x
                left_x = lm[234].x
                right_x = lm[454].x
                total_span = right_x - left_x
                yaw = ((nose_x - left_x) / (total_span or 1)) - 0.5

                # Inclinação Vertical (Pitch / Olhar para baixo no celular)
                eye_level_y = lm[168].y
                chin_y = lm[152].y
                nose_y = lm[1].y
                face_h = chin_y - eye_level_y
                pitch_ratio = (chin_y - nose_y) / (face_h or 1)
                is_looking_down = (pitch_ratio < 0.47)

                # Queda brusca da cabeça (Head Nodding)
                is_nodding = False
                if 'prev_nose_y' in locals() and prev_nose_y is not None:
                    if (nose_y - prev_nose_y) > 0.045 and ear < 0.23:
                        is_nodding = True
                prev_nose_y = nose_y

                # Detecção de olhos fechados (EAR < 0.20)
                if ear < 0.20:
                    closed_frames += 1
                else:
                    closed_frames = max(0, closed_frames - 2)

                # Detecção de bocejo (MAR > 0.48)
                if mar > 0.48:
                    yawn_frames += 1
                    if yawn_frames == 12:
                        total_yawns += 1
                else:
                    yawn_frames = max(0, yawn_frames - 1)

                # Alertas em Cascata
                if is_nodding:
                    status_text = "ALERTA: CABECA DESABANDO (COCHILO)!"
                    status_color = (0, 0, 255) # Vermelho
                elif closed_frames > 20: # ~0.8s
                    status_text = "ALERTA: MICRO-SONO / OLHOS FECHADOS!"
                    status_color = (0, 0, 255) # Vermelho
                elif is_looking_down:
                    status_text = "ALERTA: CELULAR NO COLO / OLHANDO P/ BAIXO!"
                    status_color = (0, 0, 255) # Vermelho
                elif yawn_frames > 10:
                    status_text = "ATENCAO: BOCEJO DE FADIGA!"
                    status_color = (0, 190, 255) # Laranja
                elif abs(yaw) > 0.16:
                    status_text = "ATENCAO: OLHOS FORA DA PISTA (LATERAL)!"
                    status_color = (0, 190, 255) # Laranja

                # Desenhar pontos dos olhos e boca
                eye_pts = [33, 133, 159, 145, 362, 263, 386, 374]
                for idx in eye_pts:
                    pt = (int(lm[idx].x * w), int(lm[idx].y * h))
                    cv2.circle(frame, pt, 3, status_color, -1)

                mouth_pts = [78, 13, 308, 14]
                for idx in mouth_pts:
                    pt = (int(lm[idx].x * w), int(lm[idx].y * h))
                    cv2.circle(frame, pt, 3, (0, 240, 255), -1)

                cv2.putText(frame, f"EAR (Olhos): {ear:.2f}", (30, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, f"MAR (Boca): {mar:.2f}", (30, 115),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, f"Total de Bocejos: {total_yawns}", (30, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 240, 255), 2)

            # Barra superior HUD
            cv2.rectangle(frame, (0, 0), (w, 52), (10, 15, 29), -1)
            text_x = 20
            if logo_rgba is not None:
                lh, lw = logo_rgba.shape[:2]
                ly, lx = 5, 14
                if ly + lh <= h and lx + lw <= w:
                    alpha_l = logo_rgba[:, :, 3] / 255.0
                    for c in range(3):
                        frame[ly:ly+lh, lx:lx+lw, c] = (
                            alpha_l * logo_rgba[:, :, c] +
                            (1.0 - alpha_l) * frame[ly:ly+lh, lx:lx+lw, c]
                        )
                    text_x = lx + lw + 12

            cv2.putText(frame, f"ArgosDriver AI | {status_text}", (text_x, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2, cv2.LINE_AA)

            cv2.imshow("ArgosDriver AI - Sentinela Veicular", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
