public class Toy {
    private int id;
    private int weight;
    private String name;

    public Toy(int id, int weight, String name) {
        this.id = id;
        this.weight = weight;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public int getWeight() {
        return weight;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return String.format("Игрушка \"%s\"", name);
    }

}
