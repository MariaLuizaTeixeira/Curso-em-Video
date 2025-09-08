import java.util.Scanner;
 import java.util.Locale;

public class Main {

    public static void main(String[] args) {
        Locale.setDefault(new Locale("en", "US"));
        Scanner input = new Scanner (System.in);
        double R = input.nextDouble();
        double pi = 3.14159;
        double volume = (4/3.0) * pi * R * R * R;
        System.out.printf("VOLUME = %.3f", volume);
        System.out.println();
    }
}
