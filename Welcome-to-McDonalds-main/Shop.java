public class Shop {
    public final String[] servers = {"Sam", "Obie", "Cody", "Moe", "Mateen",
        "Ali Ben Ali", "George Weinschenk", "Harvey Stenger", "Mike Lewis", "Barack Obama", "McDonald Trump"};
    public Shop() {
    }

    public void shop(Player player) {
        String server = servers[(int) Math.random() * servers.length];
        System.out.println("SHOP");
        System.out.println("Welcome to McDonald's. This is " + server + ", I'll be taking your order");
        System.out.println("You have " + player.wallet + " coins in your wallet");

        System.out.println("Here's our menu:");
        System.out.println("(1) French Fries - 15 coins (320 calories)");
        System.out.println("\tIncrease ATK by 3 and DEF by 2. Not enough salt though.");

        System.out.println("(2) Big Mac - 25 coins (600 calories)");
        System.out.println("\tPermanently increases max ATK by 3 and max DEF by 5. Just remove the weird middle bun.");

        System.out.println("(3) Vanilla Cone - 15 coins (200 calories)");
        System.out.println("\tHeals you a small amount. If only the servings were bigger.");

        System.out.println("(4) Oreo McFlurry - 30 coins (650 calories)");
        System.out.println("\tHeals you a lot, but has a small chance of giving you brain freeze. Stay frosty!"); 

        System.out.println("(5) Large Sprite - 25 coins (380 calories)");
        System.out.println("\tRemoves all negative status effects from self. Very refreshing");

        System.out.println("(6) Pink Slime - 15 coins ()");
        System.out.println("\t");

        System.out.println("(7) Happy Meal - 20 coins");

        switch (main.sc.nextInt()) {
            case
        }
    }
}