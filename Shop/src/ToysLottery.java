import java.util.ArrayList;
import java.util.List;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class ToysLottery {
    private List<Toy> toys = new ArrayList<>();
    private Random random = new Random();

    Writer2Txt writer = new Writer2Txt();
    Scanner scanner = new Scanner(System.in, "cp866");

    public void put() {

        try {
            System.out.print("Введите id: ");
            int id = Integer.parseInt(scanner.next());
            System.out.print("Введите шанс выпадения: ");
            int weight = Integer.parseInt(scanner.next());
            scanner.nextLine();
            System.out.print("Введите название: ");
            String name = scanner.nextLine();
            toys.add(new Toy(id, weight, name));
            System.out.printf("Игрушка \"%s\" добавлена с шансом %d \n", name, weight);
        } catch (InputMismatchException e) {
            System.out.println("Ошибка. Ожидалось число.");
        }

    }

    public Toy get() {
        double totalWeight = toys.stream().mapToDouble(t -> t.getWeight()).sum();
        double randomValue = random.nextDouble() * totalWeight;

        double currentWeight = 0;

        for (Toy t : toys) {
            currentWeight += t.getWeight();
            if (randomValue <= currentWeight) {
                System.out.printf("Вы выиграли %s\n", t.getName());
                toys.remove(t);
                writer.write(t);
                return t;
            }
        }
        return null;
    }

    public void info() {
        if (toys.isEmpty())
            System.out.println("Призовой фонд следует пополнить.");
        else
            System.out.println(toys);
    }

    public void addList() {
        toys.add(new Toy(1, 20, "Robot"));
        toys.add(new Toy(1, 20, "Robot"));
        toys.add(new Toy(1, 20, "Robot"));
        toys.add(new Toy(2, 20, "Doll"));
        toys.add(new Toy(2, 20, "Doll"));
        toys.add(new Toy(2, 20, "Doll"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));
        toys.add(new Toy(3, 60, "Constructor"));

    }

}
