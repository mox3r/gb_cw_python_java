import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        ToysLottery tL = new ToysLottery();
        Scanner sc = new Scanner(System.in, "cp866");

        while (true) {
            System.out.println("\033[H\033[2J");

            System.out.println("Выберите действие:");
            System.out.println("1 - Добавить в розыгрыш");
            System.out.println("2 - Испытать удачу");
            System.out.println("3 - Просмотреть список призов");
            System.out.println("0 - Выход");

            System.out.print("Ваш выбор: ");

            try {
                int choice = Integer.parseInt(sc.next());
                if (choice == 1) {
                    tL.put();
                    System.out.println("Нажмите ВВОД для продолжения...");
                    System.in.read();
                } else if (choice == 2) {
                    if (tL.get() == null)
                        tL.get();

                    System.out.println("Нажмите ВВОД для продолжения...");
                    System.in.read();
                } else if (choice == 3) {
                    tL.info();
                    System.out.println("Нажмите ВВОД для продолжения...");
                    System.in.read();
                } else if (choice == 1337) {
                    tL.addList();
                } else if (choice == 0) {
                    break;
                }
            } catch (NumberFormatException e) {
                System.out.println(e.getMessage());
                System.out.println("Ожидалось число.");
                System.console().readLine();
            }
        }
        sc.close();
    }
}
