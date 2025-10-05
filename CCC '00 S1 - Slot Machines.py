#sample input
#48
#3
#10
#4
num_quarters = int(input())
machine1 = int(input())
machine2 = int(input())
machine3 = int(input())
plays = 0

while num_quarters > 0:

    num_quarters -= 1
    machine1 += 1
    plays += 1
    if machine1 == 35:
        num_quarters += 30
        machine1 = 0

    if num_quarters == 0:
        break

    num_quarters -= 1
    machine2 += 1
    plays += 1
    if machine2 == 100:
        num_quarters += 60
        machine2 = 0

    if num_quarters == 0:
        break

    num_quarters -= 1
    machine3 += 1
    plays += 1
    if machine3 == 10:
        num_quarters += 9
        machine3 = 0



print(f"Martha plays {plays} times before going broke.")


#Random Java code cause I have it for some reason

'''
	
import java.util.Scanner;

public class SlotMachines {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values
        int quarters = scanner.nextInt();
        int machine1 = scanner.nextInt();
        int machine2 = scanner.nextInt();
        int machine3 = scanner.nextInt();

        int plays = 0;

        while (quarters > 0) {
            // Play machine 1
            quarters--;
            machine1++;
            plays++;
            if (machine1 == 35) {
                quarters += 30;
                machine1 = 0;
            }

            if (quarters == 0) break;

            // Play machine 2
            quarters--;
            machine2++;
            plays++;
            if (machine2 == 100) {
                quarters += 60;
                machine2 = 0;
            }

            if (quarters == 0) break;

            // Play machine 3
            quarters--;
            machine3++;
            plays++;
            if (machine3 == 10) {
                quarters += 9;
                machine3 = 0;
            }
        }

        System.out.println("Martha plays " + plays + " times before going broke.");
    }
}'''
