import java.util.*;

public class classy {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = Integer.parseInt(scanner.nextLine().trim());

        while (testCases-- > 0) {
            int n = Integer.parseInt(scanner.nextLine().trim());
            List<Person> people = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                String line = scanner.nextLine();
                String[] parts = line.split(": ");
                String name = parts[0];
                String classString = parts[1].replace(" class", "");
                
                people.add(new Person(name, classString));
            }

            Collections.sort(people);

            for (Person p : people) {
                System.out.println(p.name);
            }
            System.out.println("==============================");
        }
        scanner.close();
    }
}

class Person implements Comparable<Person> {
    String name;
    String classString;
    String rank;

    public Person(String name, String classString) {
        this.name = name;
        this.classString = classString;
        this.rank = generateRank(classString);
    }

    private String generateRank(String classString) {
        String[] levels = classString.split("-");
        StringBuilder rankBuilder = new StringBuilder();

        for (int i = levels.length - 1; i >= 0; i--) {
            if (levels[i].equals("upper")) rankBuilder.append("2");
            else if (levels[i].equals("middle")) rankBuilder.append("1");
            else rankBuilder.append("0");
        }

        while (rankBuilder.length() < 10) {
            rankBuilder.append("1"); // Default to middle
        }
        return rankBuilder.toString();
    }

    @Override
    public int compareTo(Person other) {
        int cmp = other.rank.compareTo(this.rank);
        return (cmp != 0) ? cmp : this.name.compareTo(other.name);
    }
}
