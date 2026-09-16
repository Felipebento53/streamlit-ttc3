import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Felipe Barboza",
    layout="wide",
    initial_sidebar_state="collapsed"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: transparent;
            overflow: hidden;
        }

        .container {
            height: 600px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .nome {
            font-family: 'Playfair Display', serif;
            font-size: 90px;
            font-weight: 700;
            letter-spacing: 3px;

            background: linear-gradient(
                90deg,
                #ff4d6d,
                #845ec2,
                #00c9a7,
                #4d96ff,
                #ff4d6d
            );

            background-size: 400% 400%;

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            animation:
                gradiente 6s ease infinite,
                aparecer 1.5s ease-out;

            text-shadow: 0px 0px 35px rgba(132, 94, 194, 0.25);
        }

        .horario {
            margin-top: 25px;
            font-family: Arial, sans-serif;
            font-size: 22px;
            color: #777;

            animation: aparecerHorario 2s ease-out;
        }

        @keyframes gradiente {
            0% {
                background-position: 0% 50%;
            }

            50% {
                background-position: 100% 50%;
            }

            100% {
                background-position: 0% 50%;
            }
        }

        @keyframes aparecer {
            from {
                opacity: 0;
                transform: translateY(40px) scale(0.9);
            }

            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        @keyframes aparecerHorario {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <div class="nome">
            Felipe Barboza
        </div>

        <div class="horario" id="horario">
            --:--:--
        </div>

    </div>

    <script>
        function atualizarHorario() {
            const agora = new Date();

            const horas = String(agora.getHours()).padStart(2, '0');
            const minutos = String(agora.getMinutes()).padStart(2, '0');
            const segundos = String(agora.getSeconds()).padStart(2, '0');

            document.getElementById("horario").innerHTML =
                `${horas}:${minutos}:${segundos}`;
        }

        atualizarHorario();

        setInterval(atualizarHorario, 1000);
    </script>

</body>
</html>
""", height=600)