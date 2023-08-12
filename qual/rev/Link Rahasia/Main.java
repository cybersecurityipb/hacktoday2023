package com;

import java.util.ArrayList;
import java.util.Base64;
import java.util.Collections;
import java.util.Scanner;

class A {
    int a[] = { 0, 23, 0, 29, 4, 29, 27, 1, 0, 9, 22, 0, 4, 28, 7, 6, 19, 24, 12, 24, 20, 6, 10, 28, 14, 16, 23, 21,
            14, 1, 23, 6, 4, 19, 23, 0, 0, 8, 7, 25, 5, 8, 12, 11, 9, 9, 2, 16, 24, 28, 17, 2, 20, 10, 24, 5, 4, 23, 23,
            17, 9, 14, 14, 15, 4, 11, 23, 1, 25, 12, 1, 4, 19, 22, 3, 25, 25, 22, 16, 28, 4, 24, 6, 10, 19, 21, 14, 7,
            19, 19, 22, 2, 24, 23, 19, 15, 4, 3, 28, 20, 19, 3, 26, 27, 19, 2, 4, 18, 15, 3, 10, 22 };
    ArrayList<Integer> b;

    A(String x) {
        b = new ArrayList<Integer>();
        a(x);
    }

    public void a(String s) {
        for (int i = s.length() - 1; i >= 0; i--) {
            int c = (int) s.charAt(i);
            for (int j = 0; j < 7; j++) {
                b.add(c % 2);
                c /= 2;
            }
        }
        Collections.reverse(b);
    }

    public int b(int idx) {
        int c = 1;
        int d = 0;
        for (int i = idx + 27; i >= idx; i--) {
            d += b.get(i) * c;
            c *= 2;
        }
        return d;
    }

    public void c() {
        int c;
        for (int i = 0; i < b.size(); i += 28) {
            int d = b(i);
            c = ((d >> 4) & 15) << 20;
            c |= ((d >> 16) & 15) << 8;
            c |= ((d >> 20) & 15) << 16;
            c |= ((d >> 12) & 15);
            c |= ((d >> 8) & 15) << 24;
            c |= (d & 15) << 12;
            c |= ((d >> 24) & 15) << 4;
            for (int j = i + 27; j >= i; j--) {
                b.set(j, c % 2);
                c /= 2;
            }
        }
    }

    public String d() {
        c();
        for (int i = 0; i < 112 && i < b.size(); i++) {
            b.set(i, (b.get(i) + a[i]) % 5);
        }

        StringBuilder c = new StringBuilder("");

        for (int i = 0; i < b.size() / 4; i++) {
            int d = 0;
            int e = 1;
            for (int j = (i + 1) * 4 - 1; j >= i * 4; j--) {
                d += e * b.get(j);
                e *= 5;
            }

            if (d > 256) {
                c.append((char) 0x3d);
            } else {
                c.append((char) d);
            }
        }
        return new String(Base64.getEncoder().encode(c.toString().getBytes()));
    }
}

class B {
    private String a;
    private String b;

    B(String checker, String input) {
        this.a = checker;
        this.b = input;
    }

    public String a(String s) {
        StringBuilder c = new StringBuilder(s);
        while (c.length() % 4 != 0) {
            c.append((char) 0x3d);
        }
        return c.toString();
    }

    public void b() {
        if (!a.equals("aHR0cHM6Ly95b3V0dS5iZS9UQlRqNHZkdHFiZw==") || b.length() > 28) {
            System.out.println("ipb.link\\link-flag");
        } else {
            A c = new A(a(b));
            if (c.d().equals(a)) {
                System.out.printf("ipb.link\\%s\n", b);
            } else {
                System.out.println("ipb.link\\link-flag");
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        String a = System.getenv("checker");
        if (a == null) {
            a = "";
        }

        System.out.print("masukkan input: ");
        Scanner b = new Scanner(System.in);
        String c = b.next();
        B d = new B(new String(Base64.getEncoder().encode(a.getBytes())), c.replace("=", ""));
        d.b();
        b.close();
    }
}