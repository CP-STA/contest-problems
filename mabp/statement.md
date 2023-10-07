# MABP

## Author

Kay Akashi

## Time (ms)

1000

## Memory (kb)

256000

## Difficulty

☆

## Tags

## Problem Statement 

Mean arterial blood pressure (MABP) can provide you with the notional average of blood pressure of an individual during each cardiac cycle. In order to calculate this value, you're usually given diastolic pressure (lowest aortic pressure when the heart is at rest) and systolic pressure (highest aortic pressure when the heart is contracting). Then, you calculate what is referred to as pulse pressure which you can calculate by subtracting diastolic pressure from systolic pressure. With those values, MABP can be calculated in a following way:

MABP = (diastolic pressure) + $\frac{1}{3}$ × (pulse pressure)

Today, Kay and his friend Haniyah are coming to the clinical placement supervised by the GP practitioner. The doctor was asking Kay to record one patient's diastolic pressure, systolic pressure, and MABP. However, Haniyah noticed that Kay wasn't writing down the patient's systolic pressure, while diastolic pressure and calculated MABP were accurately recorded. Being so kind, she added the patient's systolic pressure by calculating based on the provided values of systolic pressure and MABP to the record before submission so that Kay won't be scolded by the doctor. What was the value Haniyah added to the record?

Unit of MABP, systolic pressure, and diastolic pressure is $mmHg$.

## Constraints

$65 \leq$ MABP, systolic pressure $\leq 140$.
It is ensured that the resulting systolic pressure is higher than or equal to diastolic pressure, and is between $65$ and $140mmHg$. 
All the input values are integers.

## Input

The input consists of $2$ integers, $M$ and $D$, indicating MABP and diastolic pressure.

## Output

Output the systolic pressure in a single line. Round an answer to the nearest integer.

## Examples

### Input

```
107 98
```

### Output

```
125
```

### Explanation

When the systolic pressure is $125mmHg$ and diastolic pressure is $98mmHg$, the pulse pressure is $125 - 98 = 27mmHg$. Thus, the MABP is $98 + \frac{1}{3} × 27 = 107mmHg$ that agrees with the MABP given in input.

### Input

```
138 138
```

### Output
```
138
```

### Explanation
In healthy individuals systolic and diastolic pressures wouldn't be equal, but note that this kind of testcases might be present.