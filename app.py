from flask import Flask, render_template_string, request

app = Flask(__name__)

# Lógica pura de Python (Mantenemos la función idéntica para que tus pruebas de pytest pasen sin problemas)
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Interfaz Premium - Estilo Cybertron / Transformers
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AUTOBOT - Thermal Converter</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --cyber-blue: #00f0ff;
            --cyber-red: #ff0055;
            --matrix-dark: #0a0c10;
            --panel-bg: rgba(16, 20, 28, 0.85);
        }

        body {
            background-color: var(--matrix-dark);
            /* Fondo con patrón tecnológico sutil y gradiente cibernético */
            background-image:
                radial-gradient(at 0% 0%, rgba(0, 240, 255, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(255, 0, 85, 0.12) 0px, transparent 50%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Rajdhani', sans-serif;
            margin: 0;
            overflow: hidden;
        }

        /* Panel central estilo interfaz de Autobot/Decepticon */
        .transformer-panel {
            background: var(--panel-bg);
            border: 2px solid #1a2333;
            border-radius: 12px;
            padding: 3rem 2.5rem;
            max-width: 480px;
            width: 92%;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 40px rgba(0, 0, 0, 0.8), inset 0 0 15px rgba(0, 240, 255, 0.05);
            position: relative;
            text-align: center;
        }

        /* Esquinas decorativas de armadura robótica o HUD */
        .transformer-panel::before, .transformer-panel::after {
            content: "";
            position: absolute;
            width: 20px;
            height: 20px;
            border: 3px solid var(--cyber-blue);
        }
        .transformer-panel::before { top: -2px; left: -2px; border-right: none; border-bottom: none; }
        .transformer-panel::after { bottom: -2px; right: -2px; border-left: none; border-top: none; }

        h1 {
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-size: 1.8rem;
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
        }

        .system-status {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--cyber-blue);
            font-family: 'Orbitron', sans-serif;
            margin-bottom: 1.5rem;
            opacity: 0.8;
        }

        .description {
            color: #a4b3c6;
            font-size: 1.05rem;
            line-height: 1.4;
        }

        /* Inputs mecánicos digitales */
        .cyber-input {
            background: rgba(7, 9, 13, 0.9) !important;
            border: 1px solid #2c3a52 !important;
            color: #ffffff !important;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            letter-spacing: 1px;
            border-radius: 6px !important;
            padding: 12px !important;
            transition: all 0.3s ease !important;
        }

        .cyber-input:focus {
            border-color: var(--cyber-blue) !important;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3) !important;
        }

        /* Botón de Ignición / Activación */
        .btn-cyber {
            background: transparent;
            border: 2px solid var(--cyber-red);
            color: #ffffff;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            padding: 12px;
            border-radius: 6px;
            width: 100%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .btn-cyber:hover {
            background: var(--cyber-red);
            box-shadow: 0 0 25px rgba(255, 0, 85, 0.6);
            color: white;
            transform: translateY(-2px);
        }

        /* Pantalla de resultados tipo HUD de cabina de robot */
        .hud-display {
            background: rgba(0, 240, 255, 0.03);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-left: 4px solid var(--cyber-blue);
            border-radius: 6px;
            padding: 18px;
            margin-top: 1.5rem;
            text-align: left;
            position: relative;
        }

        .hud-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.75rem;
            color: var(--cyber-blue);
            letter-spacing: 2px;
            display: block;
            margin-bottom: 0.3rem;
            text-transform: uppercase;
        }

        .hud-data {
            font-size: 1.3rem;
            color: #ffffff;
            font-weight: 500;
        }

        .hud-data strong {
            color: var(--cyber-blue);
            font-family: 'Orbitron', sans-serif;
            text-shadow: 0 0 8px rgba(0, 240, 255, 0.4);
        }
    </style>
</head>
<body>

    <div class="transformer-panel">
        <div class="system-status">⚡ CORE OPTIMIZED // SYS ACTIVE</div>
        <h1>MATRIX CALCULATOR</h1>
        <p class="description mb-4">
            Módulo cuántico de conversión termométrica. Ingrese el vector numérico en escala Celsius para computar su salida Fahrenheit.
        </p>

        <form method="POST" action="/">
            <div class="mb-4">
                <input type="number" step="any" name="celsius" class="form-control text-center cyber-input form-control-lg" placeholder="CELSIUS VALUE" required value="{{ celsius_enviado }}">
            </div>
            <button type="submit" class="btn btn-cyber mb-2">PROCESAR VECTOR 🔄</button>
        </form>

        {% if resultado is not none %}
            <div class="hud-display text-start animate__animated animate__fadeIn">
                <span class="hud-title">🖥️ TELEMETRÍA DE SALIDA:</span>
                <div class="hud-data">
                    {{ celsius_enviado }}°C ➔ <strong>{{ resultado }}°F</strong>
                </div>
            </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    celsius_enviado = ""

    if request.method == 'POST':
        try:
            celsius_enviado = request.form.get('celsius', '')
            resultado = celsius_a_fahrenheit(float(celsius_enviado))
        except ValueError:
            resultado = "ERROR_VAL"

    return render_template_string(HTML_TEMPLATE, resultado=resultado, celsius_enviado=celsius_enviado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)