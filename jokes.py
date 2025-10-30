import java.util.Scanner;

/**
 * A simple command-line calculator in Java.
 * This program can perform basic arithmetic operations:
 * addition, subtraction, multiplication, and division.
 */
public class SimpleCalculator {

    /**
     * The main method is the entry point of the program.
     * It runs a loop to continuously ask the user for input.
     * @param args Command line arguments (not used in this program).
     */
    public static void main(String[] args) {
        // Create a Scanner object to read input from the console.
        Scanner inputScanner = new Scanner(System.in);
        // A flag to control the main application loop.
        boolean isRunning = true;

        // Display a welcome message to the user.
        printWelcomeMessage();

        // Main application loop.
        while (isRunning) {
            // Display the menu of options to the user.
            printMenu();

            // Ask the user to enter their choice.
            System.out.print("Please enter your choice (1-5): ");
            int userChoice = inputScanner.nextInt();

            // Use a switch statement to perform an action based on the user's choice.
            switch (userChoice) {
                case 1:
                    performOperation('+', inputScanner);
                    break;
                case 2:
                    performOperation('-', inputScanner);
                    break;
                case 3:
                    performOperation('*', inputScanner);
                    break;
                case 4:
                    performOperation('/', inputScanner);
                    break;
                case 5:
                    // Set the flag to false to exit the while loop.
                    isRunning = false;
                    break;
                default:
                    // Inform the user of an invalid choice.
                    System.out.println("Invalid choice. Please enter a number between 1 and 5.");
                    break;
            }
            System.out.println(); // Print a blank line for better readability.
        }

        // Display a goodbye message.
        System.out.println("Thank you for using the Simple Calculator. Goodbye!");
        // Close the scanner to prevent resource leaks.
        inputScanner.close();
    }

    /**
     * Prints the welcome message to the console.
     */
    public static void printWelcomeMessage() {
        System.out.println("======================================");
        System.out.println("    Welcome to the Simple Calculator    ");
        System.out.println("======================================");
    }

    /**
     * Prints the calculator's menu of operations.
     */
    public static void printMenu() {
        System.out.println("Please select an operation:");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.println("5. Exit");
    }

    /**
     * Performs a specified arithmetic operation based on user input.
     * @param operator The character representing the operation.
     * @param scanner  The Scanner object for reading user input.
     */
    public static void performOperation(char operator, Scanner scanner) {
        System.out.print("Enter the first number: ");
        double num1 = scanner.nextDouble();
        System.out.print("Enter the second number: ");
        double num2 = scanner.nextDouble();
        double result = 0;

        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                // Handle division by zero.
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error: Cannot divide by zero.");
                    return; // Exit the method early.
                }
                break;
        }
        System.out.println("The result is: " + result);
    }
}```
