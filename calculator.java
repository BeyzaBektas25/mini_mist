import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double sayı1, sayı2, sonuc = 0;
        boolean gecerliIslem = true;

        System.out.println("1. sayıyı giriniz: ");
        sayı1 = input.nextDouble();
        System.out.println("2. sayıyı giriniz: ");
        sayı2 = input.nextDouble();

        System.out.println("Lütfen yapacağınız işlemi giriniz (+)(-)(*)(/): ");
        char islem = input.next().charAt(0);

        switch (islem) {
            case '+':
                sonuc = sayı1 + sayı2;
                break;
            case '-':
                sonuc = sayı1 - sayı2;
                break;
            case '*':
                sonuc = sayı1 * sayı2;
                break;
            case '/':
                if (sayı2 != 0) {
                    sonuc = sayı1 / sayı2;
                } else {
                    System.out.println("HATA! Sayı 0 ile bölünemez.");
                    gecerliIslem = false;
                }
                break;
            default:
                System.out.println("Geçersiz işlem!");
                gecerliIslem = false;
        }

        if (gecerliIslem) {
            System.out.println("Sonuç: " + sonuc);
        }
    }
}
