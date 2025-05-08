from app import create_app

app = create_app()

if __name__ == '__main__':
    # Establece host='0.0.0.0' para permitir acceso desde cualquier IP
    # El debug=True permite ver errores detallados y habilita recarga automática
    app.run(debug=True, host='0.0.0.0', port=5000)

