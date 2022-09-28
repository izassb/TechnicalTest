package algorithmSolution;

import java.util.*;

public class Coins {
    private static int makeChangeCount(int total, int d) {
        int nextCoin = 0;
        switch (d) {
            case 25:
                nextCoin = 10;
                break;
            case 10:
                nextCoin = 5;
                break;
            case 5:
                nextCoin = 1;
                break;
            case 1:
                return 1; // Found a combination.Base case.
            default:
                return 0;
        }

        int ways = 0;
        for (int count = 0; count*d <= total; ++count) {
            ways += makeChangeCount(total-count*d, nextCoin);
        }
        return ways;
    }

    public static int makeChangeIterative(int total) {
        int ways = 0;
        for (int count25 = 0; count25 * 25 <= total; ++count25) {
            for (int count10 = 0; count10*10 <= total; ++count10) {
                for (int count5 = 0; count5*5 <=total; ++count5) {
                    int sum = count25*25 + count10*10 + count5*5;
                    // when the first three types of coins are selected, the way of selecting coins
                    // with denomination 1 cent has already known.
                    if (sum <= total) {
                        ++ways;
                    }
                }
            }
        }
        return ways;
    }
    public static List<Set> makeChangeList() {
        List<Set> values = new ArrayList<>(4);
        values.add(Collections.singleton(1));    // penny
        values.add(Collections.singleton(5));    // nickel
        values.add(Collections.singleton(10));   // dime
        values.add(Collections.singleton(25));   // quarter
        return values;
    }

    public static void makeChangeQuantity(int amount){
        //int[] acc = new int[4];
        List<Set> acc = new ArrayList<>();
        makeChange(amount, makeChangeList());
    }

    private static void makeChange(int amount, List<Set> acc){
        acc = makeChangeList();
        if(amount == 0){
            System.out.print("[" + acc);
            for(int i = 1; i < 4; i++){
                System.out.print(", " + acc.get(i));
            }
            System.out.print("]");
            System.out.println();
        }
        if(amount > 0){
            acc.set(0)++;
            makeChange(amount - 1, acc);
            acc.set(0)--;
            acc.get(1)++;
            makeChange(amount - 5, acc);
            acc.get(1)--;
            acc.get(2)++;
            makeChange(amount - 10, acc);
            acc.get(2)--;
            acc.get(3)++;
            makeChange(amount - 25, acc);
            acc.get(3)--;
        }
    }

    public static void main(String[] args) {
        int a = 12;
        makeChangeQuantity(a);
        makeChange(a,makeChangeList());
    }
}