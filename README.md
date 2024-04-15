## Objetivo ✨

Programar un Sokoban ❤️

## Parte 1 de 🍒 (7🟢/7)

### Colocar nuestras objetivos pricipales 🧱

- ¿Jugador existe? 🟢
- ¿Caja existe? 🟢
- ¿Meta existe? 🟢
- ¿Espacios existen? 🟢
- ¿Limites Existen? 🟢
- ¿Jugador se puede colocar sobre meta? 🟢
- ¿Caja se puede colocar en la meta? 🟢

## Parte 2 de 🍒 (8🟢/8)

### Definamos nuestras reglas 📐 

- ¿El Jugador se puede mover en cuatro direcciones? 🟢
- ¿El jugador solo puede empujar una caja? 🟢
- ¿El jugador se puede mover sobre la meta? 🟢 
- ¿El jugador puede empujar la caja sobre la meta y sacarla de la meta? 🟢 "Puede empujar la caja sobre la meta" 🟡 "al sacarla La meta desaparece"
- ¿El juego termina? 🟢
- ¿Hay muchos niveles? 🟢
- ¿Existe dificultad en el juego? 🟢

## Parte 3 de 🍒 (6🟢/6)

### Definir nuestros objetos
- 0: 🐧 # JUGADOR   
- 1: 🧱 # PAREDES
- 2: ❄️ # CAJAS
- 3: "    " # ESPACIOS
- 4: 💧 # META
- 5: 🧊 # CAJA SOBRE META     
- 6  🐧 # JUGADOR SOBRE META          
            
### Definir nuestros Movimientos (5🟢/5)
- W = Arriba ⬆️
- S = Abajo ⬇️
- A = Izquierda ⬅️
- D = Derecha ➡️
- R = Reiniciar 🔁

## Parte 4 de 🍒 (16🟢/16)

### Definamos posibilidades
| No. | Posibilidad | ¿Conseguido? |
| --- | --- | --- |
| 1. | Reiniciar el nivel | 🟢 |
| 2. | Imprimir mapas variados | 🟢 |
| 3. | Pingüino posee una habilidad especial | 🟢 |
| 4. | El juego no posee errores que afecten la jugabilidad | 🟢 |
| 5. | Movimento hacia Arriba | 🟢 |
| 6. | Movimento hacia Abajo | 🟢 |
| 7. | Movimento hacia la Derecha | 🟢 |
| 8. | Movimento hacia la Izquierda | 🟢 |
| 9. | Movimento hacia Arriba con Caja | 🟢 |
| 10. | Movimento hacia Abajo con Caja | 🟢 |
| 11. | Movimento hacia la Derecha con Caja | 🟢 |
| 12. | Movimento hacia la Izquierda con Caja | 🟢 |
| 13. | Crear mapas | 🟢 |
| 14. | Jugador regresa en sus pasos | 🟢 |
| 15. | Caja regresa junto a jugador | 🟢 |
| 16. | Jugador Tiene habilidad especial | 🟢 |

## Parte Final de 🍒 (/56)

### ¿Qué se logro?
| No. | Función | Sirve |
| --- | --- | --- |
| 0. | Cargar el siguiente nivel. | 🟢 |
| 1. | Repetir el juego hasta terminar el nivel. | 🟢 |
| 2. | Imprimir mapa.| 🟢 |
| 3. | Leer el movimiento. | 🟢 Ulitize el msvcrt para que fuera de manera automatica |
| 4. | Evaluar el movimiento del usuario. | 🟢 |
| 5. | Personaje, espacio  |🟢 | 
| 6. | Personaje, meta  | 🟢 | 
| 7. | Personaje, caja, espacio | 🟢 | 
| 8. | Personaje, caja,  meta | 🟢 | 
| 9. | Personaje, caja_meta, espacio | 🟢 | 
| 10. |Personaje, caja_meta, meta | 🟢 | 
| 11. | Personaje_meta, espacio | 🟢 | 
| 12. | Personaje_meta, meta | 🟢 | 
| 13. | Personaje_meta, caja, espacio | 🟢 | 
| 14. | Personaje_meta, caja, meta | 🟢 |
| 15. | Personaje_meta, caja_meta, espacio | 🟢 |
| 16. | Personaje_meta, caja_meta, meta | 🟢 |
| 17. | Personaje, espacio | 🟢 |
| 18. | Personaje, meta | 🟢 | 
| 19. | Personaje, caja, espacio | 🟢 | 
| 20. | Personaje, caja, meta | 🟢 | 
| 21. | Personaje, caja_meta, espacio | 🟢 | 
| 22. | Personaje, caja_meta, meta | 🟢 | 
| 23. | Personaje_meta, espacio | 🟢 | 
| 24. | Personaje_meta, meta | 🟢 | 
| 25. | Personaje_meta, caja, espacio | 🟢 |
| 26. | Personaje_meta, caja, meta | 🟢 | 
| 27. | Personaje_meta, caja_meta, espacio | 🟢 | 
| 28. | Personaje_meta, caja_meta, meta | 🟢 | 
| 29. | Personaje, espacio | 🟢 | 
| 30. | Personaje, meta | 🟢 | 
| 31. | Personaje, caja, espacio | 🟢 | 
| 32. | Personaje, caja, meta | 🟢 | 
| 33. | Personaje, caja_meta, espacio | 🟢 | 
| 34. | Personaje, caja_meta, meta | 🟢 | 
| 35. | Personaje_meta, espacio | 🟢 | 
| 36. | Personaje_meta, meta | 🟢 | 
| 37. | Personaje_meta, caja, espacio | 🟢 | 
| 38. | Personaje_meta, caja, meta | 🟢 | 
| 39. | Personaje_meta, caja_meta, espacio | 🟢 | 
| 40. | Personaje_meta, caja_meta, meta | 🟢 | 
| 41. | Personaje, espacio | 🟢 | 
| 42. | Personaje, meta | 🟢 | 
| 43. | Personaje, caja, espacio | 🟢 | 
| 44. | Personaje, caja, meta | 🟢 | 
| 45. | Personaje, caja_meta, espacio | 🟢 | 
| 46. | Personaje, caja_meta, meta | 🟢 | 
| 47. | Personaje_meta, espacio | 🟢 | 
| 48. | Personaje_meta, meta | 🟢 | 
| 49. | Personaje_meta, caja, espacio | 🟢 | 
| 50. | Personaje_meta, caja, meta | 🟢 | 
| 51. | Personaje_meta, caja_meta, espacio | 🟢 | 
| 52. | Personaje_meta, caja_meta, meta | 🟢 | 
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | 🟢 | 
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | 🟢 | 
| 55. | Función adicional o powerup (Crear metas+). | 🟢 |
