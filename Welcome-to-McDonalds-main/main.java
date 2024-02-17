import java.util.Scanner;

public class main {
    public static Scanner sc = new Scanner(System.in);
    // public static char[][] screen = {"========================================".toCharArray(),
    //                                 "|                                      |".toCharArray(),
    //                                 "|                                      |".toCharArray(),
    //                                 "|                                      |".toCharArray(),
    //                                 "|                                      |".toCharArray(),
    //                                 "|    o                                 |".toCharArray(),
    //                                 "|   <|\\                               |".toCharArray(),
    //                                 "|   / >                                |".toCharArray(),
    //                                 "========================================".toCharArray(),};
    //
    public static void clear() {
        System.out.println();
        System.out.println("Press Enter to continue.");
        sc.nextLine();
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    public static void main(String[] args) {
        // Initial object loading
        System.out.println("Welcome! Enter your name: ");
        String name = sc.nextLine();
        Player player = new Player(name, 4, 100, 10);
        System.out.println();

        System.out.println("What difficulty would you like to play on?");
        System.out.println("1: Easy");
        System.out.println("2: Medium");
        System.out.println("3: Hard");
        int difficulty = sc.nextInt();

        while (difficulty < 1 || difficulty > 3){
            System.out.print("Please input a valid difficulty: ");
            difficulty = sc.nextInt();
        }
        System.out.println();
        
        switch (difficulty) {
            case 1:{
                System.out.println("Easy difficulty has been chosen.");
                break;
            }
            case 2:{
                System.out.println("Normal difficulty has been chosen.");
                break;
            }
            case 3:{
                System.out.println("Hard difficulty has been chosen.");
                break;
            }
        }
        
        clear();
        Fight fight = new Fight(difficulty);
        
        while (fight.moreBosses()) {
            fight.fightNextBoss(player);
            //shop.show();
        }
    }

    public void updateScreen() {
        ;
    }
}