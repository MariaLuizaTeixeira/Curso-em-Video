import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class PrimeiroPrograma {
    public static void main(String[] args) {
        Locale.setDefault(new Locale("en", "US"));
        Scanner scanner = new Scanner(System.in);
        char O = scanner.next().charAt(0);
        float M[][] = new float[6][6];
        float resultado = 0;
        int limitador = 1;
        int cont = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++)
            M[i][j] = scanner.nextFloat();
        }
        
        for (int i = 0; i <= 2; i++) {
            System.out.println("i: " + i);
            for (int j = 5; j > 5 - limitador + 1; j--) {
                System.out.println("j: " + j);
                resultado+= M[i][j];
                cont++;
                System.out.println("resultado: " + resultado);   
            }
            System.out.println("saiu do j.");
            limitador++;
        }

        limitador = 1;
        
        for (int i = 5; i >= 3; i--) {
            for (int j = 5; j > 5 - limitador + 1; j--) {
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

