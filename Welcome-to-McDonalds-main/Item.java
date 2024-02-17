public class Item {
    public static final Item[] allItems = {new Item};
    public int calories;
    public int cost;
    public ItemType itemType;

    public Item(int calories, int cost, ItemType itemType) {
        this.calories = calories;
        this.cost = cost;
        this.itemType = itemType;
    }

    public String toString() {
        return this.itemType.toString();
    }
}