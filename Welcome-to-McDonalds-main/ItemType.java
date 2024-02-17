public enum ItemType {
    frenchFries,
    bigMac,
    vanillaCone,
    oreoMcFlurry,
    largeSprite,
    pinkSlime,
    happyMeal;

    public String toString() {
        switch (this) {
            case frenchFries:
                return "French Fries";
            case bigMac:
                return "Big Mac";
            case vanillaCone:
                return "Vanilla Cone";
            case oreoMcFlurry:
                return "Oreo McFlurry";
            case largeSprite:
                return "Large Sprite";
            case pinkSlime:
                return "Pink Slime";
            case happyMeal:
                return "Happy Meal";
            default:
                return "";
            }
    }
}