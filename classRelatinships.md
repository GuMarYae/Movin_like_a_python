
# Class Relationships

## 1. Association

Two classes are **related to each other**.

### Example: Student and Course

- A Student has Courses.
- A Course has Students.
- Neither owns the other.

**Think:** RELATED TO

---

## 2. Aggregation

A **weak HAS-A** relationship.

### Example: Student and Address

- A Student HAS an Address.
- The Address can exist without the Student.
- Multiple Students can share the same Address.

**Think:** HAS-A, but can exist separately.

**UML:** Empty diamond `◇`

---

## 3. Composition

A **strong HAS-A** relationship.

### Example: Student and Name

- A Student HAS a Name.
- The Name belongs specifically to that Student.
- This represents stronger ownership.

**Think:** STRONG HAS-A / OWNED

**UML:** Filled diamond `◆`

---

## 4. Inheritance

An **IS-A** relationship.

### Example: Circle and GeometricShape

- Circle IS-A GeometricShape.
- Rectangle IS-A GeometricShape.
- The child inherits from the parent.

```python
class GeometricShape:
    pass

class Circle(GeometricShape):
    pass
```
