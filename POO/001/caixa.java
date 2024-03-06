import java.util.Scanner;

public class caixa {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Qual o valor do produto? ");
        Double valor = teclado.nextDouble();
        teclado.close();

        System.out.println("Qual será a forma de pagamento?\n [1] A vista Dinheiro ou Debito10%\n [2] A vista Cartao de Credito\n [3] Duas vezes sem juros\n [4] Tres vezes juros de 10%");
        

    }

}