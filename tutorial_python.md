
# Indices negativos

-1 : se refiere al ultimo elemento.
-2 : se refiere al penultimo elemento.
-3 : se refiere al antepenultimo elemento. 
.
.
.
asi sucesivamente.

# Inputs

`input(" ")` # se usa para obtener un input.

---

# CONDICIONALES

## if, elif, else:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
```

### ELIF
se usa cuando la condicion anterior es falsa, pasa a la siguiente:

```python
if condición_1:
    # Código si condición_1 es verdadera
elif condición_2:
    # Código si condición_1 es falsa y condición_2 es verdadera
elif condición_3:
    # Código si las condiciones anteriores son falsas y condición_3 es verdadera
else:
    # Código si todas las condiciones anteriores son falsas
```

Ejemplo con notas:

```python
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")
```

---

# BUCLES

## FOR: 
Se usa para iterar sobre una secuencia (lista, diccionario, conjunto o cadenas de texto).

### Sintaxis basica:
```python
for item in iterable:
    # Bloque código
```

**iterable**: cualquier objeto sobre el que puedas iterar (listas, rangos, diccionarios, etc.)  
**item**: variable que tomara el valor de cada elemento en la secuencia uno a uno en cada iteración.

Ejemplo con range:

```python
for i in range(5):
    print(i) # Imprime del 0 al 4
```

También se puede usar `start`, `stop`, `step`:

```python
for i in range(2, 10, 2):
    print(i) # Imprime 2, 4, 6, 8
```

**Explicación:**  
El número del final (en este caso el 2) sería el `start + step`, es decir empieza en el 2, luego el 4, y así hasta 10 porque es el `stop`.

## WHILE:
Sigue ejecutando un bloque de código mientras esa condición sea verdadera.

### Sintaxis basica:

```python
while condicion:
    # Bloque código
```

La condición es evaluada antes de cada iteración. Si la condición es verdadera, el cuerpo del código seguirá ejecutándose. Si es falsa, el bucle termina.

Ejemplo:

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1 # Aseguramos que la condición eventualmente sea falsa.
```

---

# CONTROL DE FLUJO EN BUCLES:

### BREAK:  
Sale del bucle, independientemente de si la condición sigue siendo verdadera o no.

```python
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print(i)
```

### CONTINUE:
Salta la iteración actual y continúa con la siguiente iteración del bucle.

```python
for i in range(5):
    if i == 2:
        continue  # Salta el 2 y continúa con el siguiente valor
    print(i)
```

### ELSE:
Los bucles for y while pueden tener una cláusula else, que se ejecuta solo si el bucle termina sin haber sido interrumpido por un break.

```python
for i in range(5):
    print(i)
else:
    print("Bucle terminado")  # Se ejecuta solo si no se usa un `break`
```

---

# BUCLES ANIDADOS:

Es posible tener bucles dentro de otros bucles. Es útil cuando trabajas con estructuras de datos más complejas, como matrices o listas de listas.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

**Explicación detallada:**

1. Cuando `i = 0`:  
    El segundo bucle comienza y `j` toma los valores 0 y 1.  
    Primero se imprime: `i: 0, j: 0`.  
    Luego se imprime: `i: 0, j: 1`.

2. Cuando `i = 1`:  
    El segundo bucle recorre `range(2)` y `j` toma nuevamente los valores 0 y 1.  
    Primero se imprime: `i: 1, j: 0`.  
    Luego se imprime: `i: 1, j: 1`.

3. Cuando `i = 2`:  
    El segundo bucle recorre `range(2)` y `j` toma nuevamente los valores 0 y 1.  
    Primero se imprime: `i: 2, j: 0`.  
    Luego se imprime: `i: 2, j: 1`.

Resultado:

```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

---

# PASAR NUMEROS A STRING PARA SUMARLOS ENTRE SI O MAS OPERACIONES:

### Calcular la suma de los dígitos:

```python
def digit_sum(num):
    aux = 0  # Inicializamos la variable auxiliar en 0
    for x in str(num):  # Convertimos el número en cadena y recorremos cada dígito
        aux = aux + int(x)  # Convertimos el dígito en entero y lo sumamos a aux
    return aux  # Retornamos la suma total de los dígitos
```

Si el número es negativo, usamos `abs` para evitar el signo negativo:

```python
def digit_sum(num):
    return sum(int(x) for x in str(abs(num)))
```

---

# MATH

### Funciones principales:

- **Redondeo:**
    - `ceil`, `floor`, `trunc`, `round`
- **Potencias y logaritmos:**
    - `pow`, `sqrt`, `exp`, `log`, `log10`, `log2`
- **Trigonometría:**
    - `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `radians`, `degrees`
- **Combinatoria:**
    - `factorial`, `gcd`, `lcm`, `comb`, `perm`
- **Constantes:**
    - `pi`, `e`, `tau`, `inf`, `nan`

### Ejemplos de redondeo:

```python
import math
print(math.ceil(4.3))   # 5
print(math.floor(4.7))  # 4
print(math.trunc(4.9))  # 4
print(round(4.567, 2))  # 4.57
```

### Funciones de potencias y logaritmos:

```python
print(math.pow(2, 3))   # 8.0
print(math.sqrt(25))    # 5.0
print(math.exp(2))      # 7.38905609893065 (e^2)
print(math.log(10))     # 2.302585092994046 (ln 10)
print(math.log(100, 10))# 2.0 (logaritmo base 10 de 100)
```

### Funciones trigonométricas:

```python
print(math.sin(math.radians(30)))  # 0.5
print(math.cos(math.radians(60)))  # 0.5
print(math.tan(math.radians(45)))  # 1.0
print(math.degrees(math.pi))       # 180.0
```

### Funciones factoriales y combinatorias:

```python
print(math.factorial(5))  # 120 (5! = 5×4×3×2×1)
print(math.gcd(24, 36))   # 12 (MCD de 24 y 36)
print(math.lcm(4, 6))     # 12 (MCM de 4 y 6)
print(math.comb(5, 2))    # 10 (Combinaciones de 5 elementos tomados de 2 en 2)
print(math.perm(5, 2))    # 20 (Permutaciones de 5 elementos tomados de 2 en 2)
```

### Constantes matemáticas:

```python
print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586
print(math.inf > 1000000)  # True
print(math.isnan(float('nan')))  # True
```

---

# FACTORIZAR:

El factorial de un número entero positivo `n` se define como el producto de todos los números enteros desde 1 hasta `n`. Se representa con el símbolo `!n`.

Ejemplo:  
`5! = 5 × 4 × 3 × 2 × 1 = 120`
