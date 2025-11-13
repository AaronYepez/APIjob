<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscador de Alimentos</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark" style="background-image: url('{{ url_for('static', filename='/hola.jpg') }}'); background-size: cover; background-position: center center; background-attachment: fixed;">
    <div class="container mt-5">
        <div class="text-center">
            <h1 class="text-success">Buscador de Alimentos</h1>
            <p class="text-info">Encuentra información nutricional de tus alimentos favoritos</p>
        </div>

        <form method="POST" class="mt-4 mb-3">
            <div class="input-group">
                <input type="text" name="food_name" class="form-control border border-success" placeholder="Busca un alimento..." value="{{ query }}" required>
                <div class="input-group-append">
                    <button class="btn btn-success" type="submit">Buscar</button>
                </div>
            </div>
        </form>

        {% if food_data %}
            <div class="row">
                {% for food in food_data %}
                    <div class="col-md-4 mb-4">
                        <div class="card" style="background-image: url('{{ url_for('static', filename='/tarjeta.jpg') }}'); background-size: cover; background-position: center center; background-attachment: fixed;">
                            {% if food.foodImages %}
                                <img src="{{ food.foodImages[0].hostedData.mediaUrl }}" class="card-img-top" alt="{{ food.description }}">
                            {% else %}
                                <img src="https://via.placeholder.com/300" class="card-img-top" alt="Imagen no disponible">
                            {% endif %}
                            <div class="card-body">
                                <h5 class="card-title">{{ food.description }}</h5>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Marca: {{ food.brandOwner or 'No disponible' }}</li>
                                    <li class="list-group-item">Calorías: {{ food.foodNutrients[0].value if food.foodNutrients else 'N/A' }} kcal</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% elif query %}
            <div class="alert alert-warning" role="alert">
                No se encontraron resultados para "{{ query }}".
            </div>
        {% endif %}
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
