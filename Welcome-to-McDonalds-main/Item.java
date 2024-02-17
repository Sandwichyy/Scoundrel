public class Item {
    public int calories;
    public int cost;

    public Item(int calories, int cost) {
        this.calories = calories;
        this
    }

    public String toString() {
        switch (this.itemType) {
            case ItemType.frenchFries:
                return "French Fries";
            case ItemType.bigMac:
                return "Big Mac";
            case ItemType.vanillaCone:
                return "Vanilla Cone";
            case ItemType.oreoMcFlurry:
                return "Oreo McFlurry";
            case ItemType.largeSprite:
                return "Large Sprite";
            case ItemType.pinkSlime:
                return "Pink Slime";
            case ItemType.happyMeal:
                return "Happy Meal";
            default:
                return "";
            }
    }
}