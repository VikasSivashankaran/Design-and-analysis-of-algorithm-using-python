public class BinaryGCD {
    public static int findGCD(int a, int b) {
        if (a == b) {
            return a;
        }
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        int Poweroftwo = 0;
        while ((a & 1) == 0 && (b & 1) == 0) {
            a >>= 1;
            b >>= 1;
            Poweroftwo++;
        }
        while ((a & 1) == 0) {
            a >>= 1;
        }
        while ((b & 1) == 0) {
            b >>= 1;
        }
        while (a != b) {
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }
            b -= a;
        }
        return a << Poweroftwo;
    }

    public static void main(String[] args) {
        int num1 = 48;
        int num2 = 18;
        int gcd = findGCD(num1, num2);
        System.out.println("GCD:" + gcd);
    }
}
