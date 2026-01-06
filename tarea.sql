-- ============================================
-- EJERCICIOS DE BASES DE DATOS SQL
-- Base de datos: peliculas_db
-- ============================================

-- Consulta 1:
SELECT DISTINCT año FROM peliculas ORDER BY año;

-- Consulta 2:
SELECT COUNT(*) AS total FROM peliculas WHERE votos > 1000;

-- Consulta 3:
SELECT titulo, puntaje, votos FROM peliculas WHERE puntaje BETWEEN 5 AND 6;

-- Consulta 4:
SELECT nombre, apellidos FROM actores WHERE nombre LIKE '%a';

-- Consulta 5:
SELECT nombre, apellidos FROM actores WHERE nombre LIKE '%Richard%' OR apellidos LIKE '%Richard%';

-- Consulta 6:
SELECT titulo, año FROM peliculas WHERE año IN (1990, 1980, 1979) ORDER BY año;

