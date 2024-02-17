/*-------------------------------------------------
-               STUFF TO DO
-   Change attack patterns for each boss
-------------------------------------------------*/

#include <iostream>
#include <iomanip>
#include <random>
#include <string>
#include <conio.h>

using namespace std;

void setGameDifficulty(int diff); // Sets overall game difficulty
void fight();
void setBoss();
void setPlayer();
void bossTurn();
void playerTurn(int choice);

bool isNum(char num);

void clear(); // FIGURE THIS OUT

// UNCLE O'GRIMACE 1st unlocks heal
const int GRIMHP = 100; 
const int GRIMDMG = 8;

// HAMBURGLAR 2nd unlocks dagger - increased base damage
const int HAMHP = 150; 
const int HAMDMG = 10;

// OFFICER BIG MAC 3rd unlocks heavy attack
const int BIGHP = 200; 
const int BIGDMG = 12;

// MAYOR MCCHEESE 4th unlocks Chedder Armor
const int MAYHP = 250;
const int MAYDMG = 15;

// RONALD MCDONALD 5th
const int RONHP = 500; 
const int RONDMG = 25;

static int difficulty = 0;

//Player Attributes
string name = "";
float playerHP = 100;
float playerDefense = 4; // out of 8
float playerDMG = 10;

//Boss Attributes
string bossName = "";
float bossHP = 0;
float bossDMG = 0;
int bossDefense = 4;
int bossIndex = 1;

//Player unlocks
bool heal = false;
bool knife = false;
bool gun = false;
bool armor = false;

bool diffSet = false;

int turnsBeforeHeal = 0;





int main()
{
    cout << "Enter a difficulty:\n1 - Easy\n2 - Normal\n3 - Hard" << endl;
    int n;
    cin >> n;
    setGameDifficulty(n);

    cout << "\nEnter Player Name: ";
    
    cin.clear();
    cin.sync();
    getline(cin, name);

    clear();

    //Grim
    fight();


    //Ham
    fight();


    //Big
    fight();


    //May
    fight();


    //Ronny
    fight();
    cout << "Instead of falling to dust, Ronald McDonald rises once more, brushing off his shoulder, and taking off his clown costume to reveal a set of heavy armor under the lord's fake form. \n\n\tLord McDonald arises.\n" << endl;
    clear();

    //Lord Ronny
    fight();
    cout << "You feel a great increase in power emanating from the warrior before you. Once again, Lord McDonald rises to face you, growing double in size and slowly levitating off the ground. His eyes, filled with pure hatred, turn a bloodshot red, and he slowly raises his arms and bolts of electricity flows from them. \n\n\tEternal Emperor McDonald arises.\n" << endl;
    clear();

    //EE Ronny
    fight();

    return 0;
}
/*


 _______      _____     _______   _______       __________   ____ ____    ______   ____
|   _  "\   /    " \  /"       )/"       )    ("     _   ")("  _||_ " | /"      \ (\"   \|"  \  
(. |_)  :) // ____  \(:   \___/(:   \___/      )__/  \\__/ |   (  ) : ||:        ||.\\   \    | 
|:     \/ /  /    ) :)\___  \   \___  \           \\_ /    (:  |  | . )|_____/   )|: \.   \\  | 
(|  _  \\(: (____/ //  __/  \\   __/  \\          |.  |     \\ \__/ //  //      / |.  \    \. | 
|: |_)  :)\        /  /" \   :) /" \   :)         \:  |     /\\ __ //\ |:  __   \ |    \    \ | 
(_______/  \"_____/  (_______/ (_______/           \__|    (__________)|__|  \___) \___|\____\) 



*/
void bossTurn()
{
    int bossChoice = 0;
    
    if (bossIndex < 4)
    {
        switch (bossIndex)
        {
            case 1:
            {
                bossChoice = rand() % 3 + 1;
                break;
            }
            case 2:
            {
                bossChoice = rand() % 4 + 1;
                break;
            }
            case 3:
            {
                bossChoice = rand() % 5 + 1;
                break;
            }
        }
    }
    else
    {
        bossChoice = rand() % 6 + 1;
    }

    switch (bossChoice)
    {   
        //Boss Attacks
        case 1:
        { 
            cout << "Boss Attacks.\n" << endl;

            int roll = (rand() % 6) + 1;

            int turnDMG = 0;

            switch (roll)
            {
                case 1:
                {
                    cout << "Your opponent throws a jab, slightly grazing you." << endl;
                    turnDMG = bossDMG - 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 2:
                {
                    cout << "Your opponent slaps your arm with a loud clap." << endl;
                    turnDMG = bossDMG - 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 3:
                {
                    cout << "Your opponent slugs you in the stomach." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 4:
                {
                    cout << "Your opponent kicks you in the side." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 5:
                {
                    cout << "Your opponent swings a scooter at your shins." << endl;
                    turnDMG = bossDMG + 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 6:
                {
                    cout << "Your opponent whacks your alpaca." << endl;
                    turnDMG = bossDMG + 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                default:
                {
                    cout << "Stupid-ass fish" << endl;
                }
            }
            break;
        }
        //Boss Attacks
        case 2:
        {
           cout << "Boss Attacks.\n" << endl;

            int roll = (rand() % 6) + 1;

            int turnDMG = 0;

            switch (roll)
            {
                case 1:
                {
                    cout << "Your opponent throws a jab, slightly grazing you." << endl;
                    turnDMG = bossDMG - 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 2:
                {
                    cout << "Your opponent slaps your arm with a loud clap." << endl;
                    turnDMG = bossDMG - 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 3:
                {
                    cout << "Your opponent slugs you in the stomach." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 4:
                {
                    cout << "Your opponent kicks you in the side." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 5:
                {
                    cout << "Your opponent swings a scooter at your shins." << endl;
                    turnDMG = bossDMG + 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 6:
                {
                    cout << "Your opponent whacks your alpaca." << endl;
                    turnDMG = bossDMG + 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                default:
                {
                    cout << "Stupid-ass fish" << endl;
                    break;
                }
            } 
            break;
        }
        case 3:
        { 
            cout << "Boss Attacks.\n" << endl;

            int roll = (rand() % 6) + 1;

            int turnDMG = 0;

            switch (roll)
            {
                case 1:
                {
                    cout << "Your opponent throws a jab, slightly grazing you." << endl;
                    turnDMG = bossDMG - 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 2:
                {
                    cout << "Your opponent slaps your arm with a loud clap." << endl;
                    turnDMG = bossDMG - 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 3:
                {
                    cout << "Your opponent slugs you in the stomach." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 4:
                {
                    cout << "Your opponent kicks you in the side." << endl;
                    turnDMG = bossDMG;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 5:
                {
                    cout << "Your opponent swings a scooter at your shins." << endl;
                    turnDMG = bossDMG + 1;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                case 6:
                {
                    cout << "Your opponent whacks your alpaca." << endl;
                    turnDMG = bossDMG + 2;
                    cout << "\tEnemy deals " << turnDMG << " damage." << endl;
                    playerHP -= turnDMG;
                    break;
                }
                default:
                {
                    cout << "Stupid-ass fish" << endl;
                }
            }
            break;
        }
        //Boss defends
        case 4:
        {
            cout << "Boss Defends.\n" << endl;

            if (bossDefense == 8)
            {
                cout << "Your opponent has ran out of McNuggets." << endl;
                cout << "Enemy defense won't go any higher." << endl;
                break;
            }
            cout << "Your opponent pops a McNugget into his mouth and grows slightly in size." << endl;
            bossDefense++;
            playerDMG -= 2;
            cout << "\tBoss defense increases." << endl;
            break;
        }
        //Boss Demoralizes
        case 5:
        {
            cout << "Boss Demoralizes.\n" << endl;
            
            if (playerDefense == 0){
                cout << "You feel empty inside." << endl;
                cout << "Your defense won't go any lower" << endl;
                break;
            }
            cout << "Your opponent calls your mother a racial slur." << endl;
            playerDefense--;
            bossDMG += 2;
            cout << "\tPlayer defense decreases." << endl;
            break;
        }
        case 6:
        {
            cout << "Boss heals.\n" << endl;

            int healRoll = rand() % 3 + 1;

            switch (healRoll)
            {
                case 1:
                {
                    cout << "Your opponent bites a chunk of their arm and eats it. It regrows almost instantly." << endl;
                    bossHP += 4;
                    cout << "\tEnemy heals for 4 points" << endl;
                    break;
                }
                case 2:
                {
                    cout << "Your opponent bites a chunk of their arm and eats it. It regrows almost instantly." << endl;
                    bossHP += 6;
                    cout << "\tEnemy heals for 6 points" << endl;
                    break;
                }
                case 3:
                {
                    cout << "Your opponent bites a chunk of their arm and eats it. It regrows almost instantly." << endl;
                    bossHP += 8;
                    cout << "\tEnemy heals for 8 points" << endl;
                    break;
                }
            }
            break; 
        }
        default:
        {
            cout << "U actually fucking suck drop out of college" << endl;
            break;
        }
    }

    clear();
}
/*



   ________   ___            __       ___   __   ______    _____         __________   ___  ____    ______    ____  ___
  |    __ "\ |"  |          /""\     |"  \/"  |/"     "| /"      \     ("     _   ")("  _||_ " | /"      \ (\"   \|"  \     
  (. |__) :)||  |         /    \     \   \  /(: ______)|:        |     )__/  \\__/ |   (  ) : ||:        ||.\\   \    |    
  |:  ____/ |:  |        /' /\  \     \\  \/  \/    |  |_____/   )        \\_ /    (:  |  | . )|_____/   )|: \.   \\  |    
  (|  /      \  |___    //  __'  \    /   /   // ___)_  //      /         |.  |     \\ \__/ //  //      / |.  \    \. |    
 /|__/ \    ( \_|:  \  /   /  \\  \  /   /   (:      "||:  __   \         \:  |     /\\ __ //\ |:  __   \ |    \    \ |    
(_______)    \_______)(___/    \___)|___/     \_______)|__|  \___)         \__|    (__________)|__|  \___) \___|\____\)




*/
void playerTurn(int choice)
{
    int roll = (rand() % 6) + 1;

    switch (choice)
    {
        //Player choice is attack
        case 49:
        {
            cout << "You chose Attack\n" << endl;
            
            int turnDMG = 0;

            switch (roll)
            {
                case 1:
                {
                    cout << "You throw a jab, slightly grazing you opponent." << endl;
                    turnDMG = playerDMG - 2;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                case 2:
                {
                    cout << "Your opponent braces as you swipe left on their tinder profile." << endl;
                    turnDMG = playerDMG - 1;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                case 3:
                {
                    cout << "You kick your opponent in the shins with all your might." << endl;
                    turnDMG = playerDMG;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                case 4:
                {
                    cout << "You slug you opponent, landing a blow directly to their face." << endl;
                    turnDMG = playerDMG;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                case 5:
                {
                    cout << "You faint your attack and land an uppercut on you unsuspecting opponent." << endl;
                    turnDMG = playerDMG + 1;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                case 6:
                {
                    cout << "You slam your opponent's limb in the car door, discombobulating them." << endl;
                    turnDMG = playerDMG + 2;
                    bossHP -= turnDMG;
                    cout << "\tYou deal " << turnDMG << " damage." << endl;
                    break;
                }
                default:
                {
                    cout << "Stupid-ass monkey" << endl;
                }
                break;
            }
            break;
        }
        //Player choice is defend
        case 50:
        {
            cout << "You chose Defend\n" << endl;

            if (playerDefense == 8)
            {
                cout << "The homeless man ran out of pillows." << endl;
                cout << "Defense won't go any higher" << endl;
                break;
            }

            cout << "You steal the homeless man's pillow and duct tape it to yourself." << endl;
            playerDefense++;
            bossDMG -= 2;
            cout << "\tYour defense increases." << endl;
            break;
        }
        //Player choice is demoralize
        case 51:
        {
            if (bossDefense == 0)
            {
                cout << "Your opponent is depressed." << endl;
                cout << "Enemy defense won't go any lower" << endl;
                break;
            }
            cout << "You chose Taunt\n" << endl;
            cout << "You call your opponent fat, enraging them." << endl;
            bossDefense--;
            playerDMG += 2;
            cout << "\tEnemy defense decreases." << endl;
            break;
        }
        //Player choice is heal
        case 52:
        {
            if (turnsBeforeHeal == 0)
            {
                cout << "You reach into your bottomless pocket, pulling out a green steak and inhaling it with great speed." << endl;
                int healRoll = rand() % 3 + 1;
                switch (healRoll)
                {
                    case 1:
                    {
                        cout << "\tYou heal for 4 points." << endl;
                        playerHP += 4;
                        break;
                    }
                    case 2:
                    {
                        cout << "\tYou heal for 6 points." << endl;
                        playerHP += 6;
                        break;
                    }
                    case 3:
                    {
                        cout << "\tYou heal for 8 points." << endl;
                        playerHP += 8;
                        break;
                    }
                    default:
                    {
                        cout << "How tf u gonna be a doctor if u cant debug this shit goddamn." << endl;
                        break;
                    }
                }
                turnsBeforeHeal++;
            }
            else
            {
                cout << "You reach into your pocket to find there is no green steak." << endl;
                cout << "\tHeal cooldown: " << 2 -turnsBeforeHeal + 1 << " turns." << endl;
                turnsBeforeHeal++;
                if(turnsBeforeHeal == 3)
                {
                    turnsBeforeHeal = 0;
                }
            }
            break;
        }
        //For use by developer to save time in testing
        case 64:
        {
            cout << "Peeking under the hood I see." << endl;
            playerHP = 0;
            break;
        }
        case 38:
        {
            cout << "Peeking under the hood I see." << endl;
            bossHP = 0;
            break;
        }
    }
    if (bossHP <= 0) 
    {
        cout << "\n\n\t\tYou defeated " << bossName << "." << endl;
    }
    else
    {
        clear();
    }
}
/*



 _______       __       ___      ___   _______      ________   __     _______   _______  __     ______   ____  ____  ___  ___________  ___  ___  
 /" _   "|     /""\     |"  \    /"  | /"     "|    |"      "\ |" \   /"     "| /"     "||" \   /" _  "\ ("  _||_ " ||"  |("     _   ")|"  \/"  | 
(: ( \___)    /    \     \   \  //   |(: ______)    (.  ___  :)||  | (: ______)(: ______)||  | (: ( \___)|   (  ) : |||  | )__/  \\__/  \   \  /  
 \/ \        /' /\  \    /\\  \/.    | \/    |      |: \   ) |||:  |  \/    |   \/    |  |:  |  \/ \     (:  |  | . )|:  |    \\_ /      \\  \/   
 //  \ ___  //  __'  \  |: \.        | // ___)_     (| (___\ |||.  |  // ___)   // ___)  |.  |  //  \ _   \\ \__/ //  \  |___ |.  |      /   /    
(:   _(  _|/   /  \\  \ |.  \    /:  |(:      "|    |:       :)/\  |\(:  (     (:  (     /\  |\(:   _) \  /\\ __ //\ ( \_|:  \\:  |     /   /     
 \_______)(___/    \___)|___|\__/|___| \_______)    (________/(__\_|_)\__/      \__/    (__\_|_)\_______)(__________) \_______)\__|    |___/   




*/
void setGameDifficulty(int diff)
{
    
    while (diffSet != true)
    {
        if (diff == 1 || diff == 2 || diff == 3)
        {
            switch (diff)
            {
                case 1: 
                {
                    cout << "Difficulty has been set to easy. If you manage to die then you actually suck." << endl;
                    difficulty = diff;
                    diffSet = true;
                    break;
                }
                case 2: 
                {
                    cout << "Difficulty has been set to normal. This is the way the game is meant to be played. Have fun." << endl;
                    difficulty = diff;
                    diffSet = true;
                    break;
                }
                case 3: 
                {
                    cout << "Difficulty has been set to hard. Pain, without love. Pain, can't get enough." << endl;
                    difficulty = diff;
                    diffSet = true;
                    break;
                }
                default:
                {
                    cout << "Fix ur game dumbass" << endl;
                    break;
                }
            }
        }
        else
        {
            cout << "Please enter a correct difficulty:\n1 - Easy\n2 - Normal\n3 - Hard" << endl;
            cin >> diff;
        }
    }
}
/*



  ______   ___       _______       __        _______   
 /" _  "\ |"  |     /"     "|     /""\      /"      \  
(: ( \___)||  |    (: ______)    /    \    |:        | 
 \/ \     |:  |     \/    |     /' /\  \   |_____/   ) 
 //  \ _   \  |___  // ___)_   //  __'  \   //      /  
(:   _) \ ( \_|:  \(:      "| /   /  \\  \ |:  __   \  
 \_______) \_______)\_______)(___/    \___)|__|  \___)





*/
void clear()
{
    //FIGURE THIS OUT
    cout << "Press any key to continue...";
    getch();
    for (int i = 0; i < 100; i++){
        cout << "\n";
    }
    cout << endl;
}
/*



  _______  __     _______    __    __  ___________  
 /"     "||" \   /" _   "|  /" |  | "\("     _   ") 
(: ______)||  | (: ( \___) (:  (__)  :))__/  \\__/  
 \/    |  |:  |  \/ \       \/      \/    \\_ /     
 // ___)  |.  |  //  \ ___  //  __  \\    |.  |     
(:  (     /\  |\(:   _(  _|(:  (  )  :)   \:  |     
 \__/    (__\_|_)\_______)  \__|  |__/     \__|   





*/
void fight()
{
    setBoss();
    setPlayer();

    while(bossHP > 0)
    {
        if (playerHP > 0)
        {
            char choice = 0;
            cout << name << ": " << playerHP << endl << endl;
            cout << bossName << ": " << bossHP << endl << endl;
            cout << "What will you do? :" << endl << endl;
            cout << "\t (1) Attack" << endl;
            cout << "\t (2) Defend" << endl;
            cout << "\t (3) Taunt" << endl;
            if (heal == true)
                cout << "\t (4) Heal" << endl;
            cout << "\n Your move: ";
            cin >> choice;

            if (choice != '@' && choice != '&')
            {
                if (choice > 52 || choice < 49) {
                    while (choice < 49 || choice > 52)
                    {
                        cout << "Please enter a correct choice: ";
                        cin >> choice;
                    }
                }
            }

            
            playerTurn(choice);

            if (bossHP > 0 && playerHP > 0)
                bossTurn();
        }
        else
        {
            char yorn;
            cout << "Game over" << endl;
            cout << "Continue? (y or n)" << endl;
            cin >> yorn;

            if (yorn == 121)
            {
                clear();
                return;
            }
            else if (yorn == 110)
            {
                clear();
                cout << "Created by Abdulmateen Shaikh." << endl;
                cout << "Thank you for playing!" << endl;
                abort();
            }
            else
            {
                while (yorn != 110 || yorn != 121)
                {
                    cout << "Please enter a correct input (y for yes and n for no): " << endl;
                    cin >> yorn; 
                }
            }
        }
    }
    bossIndex++;

    clear();

    if(bossIndex > 1)
        heal = true;
}
/*



 _______     ______    ________  ________       ________  _______  ___________  ____  ____    _______   
|   _  "\   /    " \  /"       )/"       )     /"       )/"     "|("     _   ")("  _||_ " |  |   __ "\  
(. |_)  :) // ____  \(:   \___/(:   \___/     (:   \___/(: ______) )__/  \\__/ |   (  ) : |  (. |__) :) 
|:     \/ /  /    ) :)\___  \   \___  \        \___  \   \/    |      \\_ /    (:  |  | . )  |:  ____/  
(|  _  \\(: (____/ //  __/  \\   __/  \\        __/  \\  // ___)_     |.  |     \\ \__/ //   (|  /      
|: |_)  :)\        /  /" \   :) /" \   :)      /" \   :)(:      "|    \:  |     /\\ __ //\  /|__/ \     
(_______/  \"_____/  (_______/ (_______/      (_______/  \_______)     \__|    (__________)(_______)  






*/
void setBoss()
{
    switch (difficulty)
    {
        case 1:
        {
            if (bossIndex == 1)
            {
                bossName = "Uncle O'Grimace";
                bossHP = GRIMHP * .75;
                bossDMG = GRIMDMG * .75;
            }
            else if (bossIndex == 2)
            {
                bossName = "The Hamburglar";
                bossHP = HAMHP * .75;
                bossDMG = HAMDMG * .75;
            }
            else if (bossIndex == 3)
            {
                bossName = "Officer Big Mac";
                bossHP = BIGHP * .75;
                bossDMG = BIGDMG * .75;
            }
            else if (bossIndex == 4)
            {
                bossName = "Mayor McCheese";
                bossHP = MAYHP * .75;
                bossDMG = MAYDMG * .75;
            }
            else if (bossIndex == 5)
            {
                bossName = "Ronald McDonald";
                bossHP = RONHP * .75;
                bossDMG = RONDMG * .75;
            }
            else if (bossIndex == 6){
                bossName = "Lord McDonald";
                bossHP = (RONHP + 100) * .75;
                bossHP = (RONDMG + 5) * .75;
            }
            else
            {
                bossName = "Eternal Emperor Ronald McDonald";
                bossHP = (RONHP + 250) * .75;
                bossHP = (RONDMG + 10) * .75;
            }
            break;
        }
        case 2:
        {
            if (bossIndex == 1)
            {
                bossName = "Uncle O'Grimace";
                bossHP = GRIMHP;
                bossDMG = GRIMDMG;
            }
            else if (bossIndex == 2)
            {
                bossName = "The Hamburglar";
                bossHP = HAMHP;
                bossDMG = HAMDMG;
            }
            else if (bossIndex == 3)
            {
                bossName = "Officer Big Mac";
                bossHP = BIGHP;
                bossDMG = BIGDMG;
            }
            else if (bossIndex == 4)
            {
                bossName = "Mayor McCheese";
                bossHP = MAYHP;
                bossDMG = MAYDMG;
            }
            else if (bossIndex == 5)
            {
                bossName = "Ronald McDonald";
                bossHP = RONHP;
                bossDMG = RONDMG;
            }
            else if (bossIndex == 6){
                bossName = "Lord McDonald";
                bossHP = (RONHP + 100);
                bossDMG = (RONDMG + 5);
            }
            else
            {
                bossName = "Eternal Emperor Ronald McDonald";
                bossHP = (RONHP + 250);
                bossDMG = (RONDMG + 10);
            }
          break;
        }
        case 3:
        {
            if (bossIndex == 1)
            {
                bossName = "Uncle O'Grimace";
                bossHP = GRIMHP * 1.5;
                bossDMG = GRIMDMG * 1.5;
            }
            else if (bossIndex == 2)
            {
                bossName = "The Hamburglar";
                bossHP = HAMHP * 1.5;
                bossDMG = HAMDMG * 1.5;
            }
            else if (bossIndex == 3)
            {
                bossName = "Officer Big Mac";
                bossHP = BIGHP * 1.5;
                bossDMG = BIGDMG * 1.5;
            }
            else if (bossIndex == 4)
            {
                bossName = "Mayor McCheese";
                bossHP = MAYHP * 1.5;
                bossDMG = MAYDMG * 1.5;
            }
            else if (bossIndex == 5)
            {
                bossName = "Ronald McDonald";
                bossHP = RONHP * 1.5;
                bossDMG = RONDMG * 1.5;
            }
            else if (bossIndex == 6){
                bossName = "Lord McDonald";
                bossHP = (RONHP + 100) * 1.5;
                bossDMG = (RONDMG + 5) * 1.5;
            }
            else
            {
                bossName = "Eternal Emperor Ronald McDonald";
                bossHP = (RONHP + 250) * 1.5;
                bossDMG = (RONDMG + 10) * 4.5;
            }
          break;
        }
    }
}
/*



   _______   ___            __       ___  ___  _______   _______        ________  _______  ___________  ____  ____    _______   
  |   __ "\ |"  |          /""\     |"  \/"  |/"     "| /"      \      /"       )/"     "|("     _   ")("  _||_ " |  |   __ "\  
  (. |__) :)||  |         /    \     \   \  /(: ______)|:        |    (:   \___/(: ______) )__/  \\__/ |   (  ) : |  (. |__) :) 
  |:  ____/ |:  |        /' /\  \     \\  \/  \/    |  |_____/   )     \___  \   \/    |      \\_ /    (:  |  | . )  |:  ____/  
  (|  /      \  |___    //  __'  \    /   /   // ___)_  //      /       __/  \\  // ___)_     |.  |     \\ \__/ //   (|  /      
 /|__/ \    ( \_|:  \  /   /  \\  \  /   /   (:      "||:  __   \      /" \   :)(:      "|    \:  |     /\\ __ //\  /|__/ \     
(_______)    \_______)(___/    \___)|___/     \_______)|__|  \___)    (_______/  \_______)     \__|    (__________)(_______)






*/
void setPlayer()
{
    playerHP = 100;
    playerDefense = 4;
    playerDMG = 10;
    if (knife == true)
    {
        playerDMG = 15;
    }
    if (armor == true)
    {
        playerHP = 150;
        playerDefense = 5;
    }
}

bool isNum(char num){
    if(!isdigit(num))
        return false;
    return true;
}