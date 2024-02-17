public class Entity {
    public final String[] insults = {"stupid", "ugly", "annoying", "short", "a cs major", "mid", "fat", "maidenless", "broke", "stinky"};
    public String name;
    public int defense;
    public double health;
    public double damage;
    public StatusEffect statusEffect;

    public Entity() {
        this.name = "";
        this.defense = 4;
        this.health = 100.0f;
        this.damage = 15.00f;
        this.statusEffect = StatusEffect.none;
    }

    public Entity(String name, int defense, double health, double damage) {
        this.name = name;
        this.defense = defense;
        this.health = health;
        this.damage = damage;
        this.statusEffect = StatusEffect.none;
    }

    public void giveStatus(StatusEffect s){
        this.statusEffect = s;
    }
    
    public void taunt(Entity e) {
        if (e.defense > 0) {
            e.defense -= 1;
            this.damage += 2;
            String insult = insults[(int) Math.random() * insults.length];
            System.out.println("Your opponent called you " + insult + ". Defense decreased.");
        } else {
            //System.out.println("Enemy defense cannot be lowered further.");
        }
    }
    
    public void defend(Entity e) {
        if (this.defense < 8) {
            this.defense += 1;
            e.damage -= 2;
            System.out.println("Your opponent tapes a layer of pillows to himself. Enemy defense increased.");
        } else {
            //System.out.println("Your defense cannot go higher.");
        }
    }

    public void attack(Entity e) {
        int roll = (int) Math.random() * 6 + 1;
        double turnDmg = this.damage;       
        switch (roll) {
            case 1:{
                System.out.println("Your opponent throw a jab, slightly grazing your opponent.");
                turnDmg -= 2;
                break;
            }
            case 2:{
                System.out.println("Your opponent slaps you across the face three times.");
                turnDmg -= 1;
                break;
            }
            case 3:
            case 4:{
                System.out.println("Your opponent gives you a swirlie.");
                //turnDmg = this.damage;
                break;
            }
            case 5:{
                System.out.println("Your opponent sweeps you off your feet.");
                turnDmg += 1;
                break;
            }
            case 6:{
                System.out.println("Your opponent belly flops on your legs, incapacitating you.");
                turnDmg += 2;
                break;
            }
        }
        System.out.println("Enemy deals " + turnDmg + " damage.");
        this.health -= turnDmg;
    }
}