import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(new Locale("en", "US"));
        Scanner scanner = new Scanner(System.in);
        char O = scanner.next().charAt(0);
        float M[][] = new float[12][12];
        float resultado = 0;
        int limitador = 1;
        int cont = 0;
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 12; j++)
            M[i][j] = scanner.nextFloat();
        }
        
        for (int i = 0; i <= 5; i++) {
            for (int j = 11; j > j - limitador + 1; j--) {
                resultado+= M[i][j];
                cont++;
                System.out.println(resultado);
            }
            limitador++;
        }

        limitador = 1;
        
        for (int i = 11; i >= 6; i--) {
            for (int j = 11; j > j - limitador + 1; j--) {
                resultado+= M[i][j];
                cont++;
                System.out.println(resultado);
            }
            limitador++;
        }

        if (O == 'M') {
            resultado/= cont;
        }
        System.out.printf("%.1f", resultado);
        System.out.println();
    }
}

