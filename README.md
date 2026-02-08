# SCaRUBBING

A beginner programming exercise written on **November, 2021** as an early practice project when first learning to code.

## Purpose
Simulate a brush-equipped toy car moving on an $N \times N$ grid, drawing patterns based on command inputs. Implements basic concepts like loops, conditionals, state management, and toroidal boundary wrapping.

## Usage
```bash
python3 assignment2.py
```
Enter commands separated by `+`:
```
5+3+1+5_3+1+3+5_2+6+2+5_2+1+7+5_4+5_3+8+0
```
<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP 
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT
