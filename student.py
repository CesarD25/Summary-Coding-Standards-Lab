"""Student Grade Management System."""

from typing import List, Union


class Student:
    """Manages student records and academic grades."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize student instance."""
        self.student_id = student_id.strip() if isinstance(student_id, str) else ""
        self.name = name.strip() if isinstance(name, str) else ""
        self.grades: List[float] = []

        if not self.student_id or not self.name:
            print(f"[Error] ID '{student_id}' and Name '{name}' must be non-empty.")

    def add_grade(self, grade: Union[int, float]) -> bool:
        """Add numeric grade between 0 and 100."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print(f"[Error] Grade '{grade}' must be numeric.")
            return False
        if not 0 <= grade <= 100:
            print(f"[Error] Grade {grade} out of bounds (0-100).")
            return False
        self.grades.append(float(grade))
        return True

    def calculate_average(self) -> float:
        """Calculate average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        """Determine letter grade."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    @property
    def is_passed(self) -> str:
        """Determine pass or fail status."""
        return "Passed" if self.calculate_average() >= 60 else "Failed"

    @property
    def is_honor_roll(self) -> bool:
        """Determine honor roll eligibility."""
        return self.calculate_average() >= 90

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove grade by index."""
        if isinstance(index, bool) or not isinstance(index, int):
            print(f"[Error] Index '{index}' must be an integer.")
            return False
        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"[Success] Removed grade {removed} at index {index}.")
            return True
        print(f"[Error] Index {index} is out of bounds.")
        return False

    def remove_grade_by_value(self, grade: Union[int, float]) -> bool:
        """Remove grade by numeric value."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print(f"[Error] Value '{grade}' must be numeric.")
            return False
        target = float(grade)
        if target in self.grades:
            self.grades.remove(target)
            print(f"[Success] Removed grade {target}.")
            return True
        print(f"[Error] Grade {target} not found.")
        return False

    def generate_report(self) -> None:
        """Print formatted summary report."""
        sep = "=" * 48
        print(sep)
        print(f" STUDENT SUMMARY REPORT: {self.name.upper() or 'UNKNOWN'}")
        print(sep)
        print(f" Student ID:        {self.student_id or 'N/A'}")
        print(f" Student Name:      {self.name or 'N/A'}")
        print(f" Number of Grades:  {len(self.grades)}")
        print(f" Average Grade:     {self.calculate_average():.2f}")
        print(f" Letter Grade:      {self.get_letter_grade()}")
        print(f" Pass/Fail Status:  {self.is_passed}")
        print(f" Honor Roll:        {self.is_honor_roll}")
        print(sep)


def main() -> None:
    """Demonstrate student grade management functionality."""
    student_a = Student("20260101", "Alice Smith")
    student_a.add_grade(95.0)
    student_a.add_grade(88.5)
    student_a.add_grade(92.0)
    student_a.generate_report()

    student_a.remove_grade_by_index(1)
    student_a.remove_grade_by_value(92.0)
    student_a.generate_report()

    student_b = Student("20260102", "Bob Jones")
    student_b.add_grade("Fifty")
    student_b.add_grade(150.0)
    student_b.add_grade(-15.0)
    student_b.remove_grade_by_index(99)
    student_b.remove_grade_by_value(50.0)
    student_b.add_grade(55.0)
    student_b.generate_report()

    student_c = Student("", "")
    student_c.generate_report()


if __name__ == "__main__":
    main()
    