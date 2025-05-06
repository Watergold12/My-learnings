import java.io.; import java.util.;

class Student implements Serializable { private static final long serialVersionUID = 1L; int id; String name; int age;

public Student(int id, String name, int age) {
    this.id = id;
    this.name = name;
    this.age = age;
}

@Override
public String toString() {
    return "ID: " + id + ", Name: " + name + ", Age: " + age;
}

}

public class StudentManagementSystem { static final String FILE_NAME = "students.dat"; static List<Student> students = new ArrayList<>();

public static void main(String[] args) {
    loadFromFile();
    Scanner scanner = new Scanner(System.in);
    int choice;
    do {
        System.out.println("\n--- Student Management System ---");
        System.out.println("1. Add Student");
        System.out.println("2. Remove Student");
        System.out.println("3. Update Student");
        System.out.println("4. Search Student");
        System.out.println("5. Display All Students");
        System.out.println("6. Exit");
        System.out.print("Enter your choice: ");
        choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
            case 1 -> addStudent(scanner);
            case 2 -> removeStudent(scanner);
            case 3 -> updateStudent(scanner);
            case 4 -> searchStudent(scanner);
            case 5 -> displayAll();
            case 6 -> saveToFile();
            default -> System.out.println("Invalid choice!");
        }
    } while (choice != 6);

    scanner.close();
}

static void addStudent(Scanner scanner) {
    System.out.print("Enter ID: ");
    int id = scanner.nextInt();
    scanner.nextLine();
    System.out.print("Enter name: ");
    String name = scanner.nextLine
