
import java. util. Random;

class Game
{
	// to generate random number from fixed array
	int generateRandomNumber() 
	{
		int array[] = {1,0,2,0,3,0,4,0,5,5,0};
		int rnd = new Random().nextInt(array.length);
		return array[rnd];
	}

	public static void main(String args[])
	{
		int user_account = 1000;
		int bet_point = 10;
		int random_number;
		int win_amount;
		Game game = new Game();

		// loop for 1000 bet
		for(int i=0;i<1000;i++)
		{
			random_number = game.generateRandomNumber();
			user_account = user_account - 10;
			win_amount = 10 * random_number;
			user_account = user_account + win_amount;
			System.out.println("Bet no. " + (i+1) + " :You have won "+win_amount+" points, " + "Current score = " + user_account);
		}
		System.out.println("you have "+user_account+" points in your account");
	}
}