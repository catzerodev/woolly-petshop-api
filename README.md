# 🐑 Woolly PetShop

Aplicación **Full Stack** desarrollada como parte de un Bootcamp Full Stack.

El proyecto consiste en una tienda de mascotas compuesta por un **frontend en React** y una **API REST en Flask**, conectados a una base de datos PostgreSQL.

La arquitectura del backend está organizada por capas utilizando **Resources**, **Services** y **Models**, siguiendo principios de separación de responsabilidades.

---

## 🚀 Tecnologías

### Backend

- Python
- Flask
- Flask RESTful
- SQLAlchemy
- PostgreSQL
- Flask-JWT-Extended
- Pydantic
- Alembic

### Frontend

- React
- Vite
- Tailwind CSS
- Zustand

---

## ✨ Características

- 🔐 Autenticación con JWT.
- 📦 CRUD de productos.
- 🗂️ CRUD de categorías.
- 📈 Endpoint de lógica de negocio para reabastecer stock.
- 🛒 Integración con un frontend desarrollado en React.
- 🔎 Búsqueda y filtrado de productos por categoría.
- ✅ Validaciones con Pydantic.
- 📚 Documentación interactiva con Swagger.
- 🐘 Base de datos PostgreSQL.

---

## 🏗️ Arquitectura

```
React (Vite)
      │
      ▼
 Flask REST API
      │
      ▼
 SQLAlchemy
      │
      ▼
 PostgreSQL
```

---

## ▶️ Ejecución

### Backend

```bash
python run.py
```

Servidor:

```
http://127.0.0.1:5000
```

### Frontend

```bash
npm install
npm run dev
```

Servidor de desarrollo:

```
http://localhost:5173
```

---

## 📖 Documentación

Swagger disponible en:

```
http://127.0.0.1:5000/apidocs
```