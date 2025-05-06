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
    String name = scanner.nextLine();
    System.out.print("Enter age: ");
    int age = scanner.nextInt();
    students.add(new Student(id, name, age));
    System.out.println("Student added successfully.");
}

static void removeStudent(Scanner scanner) {
    System.out.print("Enter ID to remove: ");
    int id = scanner.nextInt();
    students.removeIf(s -> s.id == id);
    System.out.println("Student removed (if existed).\n");
}

static void updateStudent(Scanner scanner) {
    System.out.print("Enter ID to update: ");
    int id = scanner.nextInt();
    scanner.nextLine();
    for (Student s : students) {
        if (s.id == id) {
            System.out.print("Enter new name: ");
            s.name = scanner.nextLine();
            System.out.print("Enter new age: ");
            s.age = scanner.nextInt();
            System.out.println("Student updated.");
            return;
        }
    }
    System.out.println("Student not found.");
}

static void searchStudent(Scanner scanner) {
    System.out.print("Enter ID to search: ");
    int id = scanner.nextInt();
    for (Student s : students) {
        if (s.id == id) {
            System.out.println(s);
            return;
        }
    }
    System.out.println("Student not found.");
}

static void displayAll() {
    if (students.isEmpty()) {
        System.out.println("No student records found.");
    } else {
        students.forEach(System.out::println);
    }
}

static void saveToFile() {
    try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(FILE_NAME))) {
        out.writeObject(students);
        System.out.println("Data saved successfully.");
    } catch (IOException e) {
        System.out.println("Error saving data: " + e.getMessage());
    }
}

static void loadFromFile() {
    File file = new File(FILE_NAME);
    if (!file.exists()) return;
    try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(file))) {
        students = (List<Student>) in.readObject();
    } catch (IOException | ClassNotFoundException e) {
        System.out.println("Error loading data: " + e.getMessage());
    }
}

}
