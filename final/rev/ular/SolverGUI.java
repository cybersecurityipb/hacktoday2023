package com.ular;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Random;

public class SolverGUI extends JPanel implements KeyListener {
    private GameLogic gameLogic;

    public SolverGUI(int frameWidth, int frameHeight) {
        gameLogic = new GameLogic(frameWidth, frameHeight);

        // Add the KeyListener to the panel
        addKeyListener(this);
        setFocusable(true);

        // Create a timer to update the animation
        Timer timer = new Timer(50, e -> {
            gameLogic.updateGame();
            repaint();
        });
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        gameLogic.draw(g);
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        gameLogic.processKeyPress(key);
    }

    @Override
    public void keyTyped(KeyEvent e) {
        // Not used in this example
    }

    @Override
    public void keyReleased(KeyEvent e) {
        // Not used in this example
    }

    public static void main(String[] args) {
        int frameWidth = 600;
        int frameHeight = 600;

        JFrame frame = new JFrame("ULAR");
        URL imageUrl = SolverGUI.class.getResource("/com/images/Ular.png");
        ImageIcon icon = new ImageIcon(imageUrl);
        frame.setIconImage(icon.getImage());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create an instance of the animation panel
        SolverGUI gui = new SolverGUI(frameWidth, frameHeight);
        frame.add(gui);

        // Set the size and make the frame unresizable
        frame.setSize(frameWidth, frameHeight);
        frame.setResizable(false);

        // Center the frame on the screen
        frame.setLocationRelativeTo(null);

        // Make the frame visible and request focus for the panel
        frame.setVisible(true);
        frame.setLayout(null);
        gui.requestFocus();
    }
}

interface Drawable {
    int OBJECT_SIZE = 15;
    int MOVE_AMOUNT = 15;
    int innerFrameWidth = 345;
    int innerFrameHeight = 405;
    int innerFrameX = 120;
    int innerFrameY = 120;

    void draw(Graphics g);
}

class GameLogic implements Drawable {
    private Random random;
    private int xVelocity;
    private int yVelocity;
    private boolean isMoving;
    private boolean gameOver;
    private int frameWidth;
    private int frameHeight;
    private int highscore;
    private boolean solved;
    private static final String key = "comp";
    private Integer[] en = { -8404974, 1577218993, -213184724, -331723495, 571151672, -2013750696, -1650386467,
            -1737588285, 570046536, -1966666470, 1154404952, -1748428996, 1905678622, 2059689707, -1036153661,
            832098208, 1055321998, 741327372, -184639855, -1498573684, 843587184, 999733815, 1891293215, 1571063152,
            -1727372612, 40176893, -1853095029, -1266238874, -1877391967, 1516011065, 282540859, 2028814664, 407765662,
            -832013141, -514317271, 1478103917, -1091672068, -266629001, -1023775920, -739728588, -1339605833,
            761476080, -618656445, 1158875663, 1381307935, -2082437695, -1329051471, 261422631, -1763353666,
            -2061834004, 1324632140, -624540660, -607857198, 581670240, 1877205563, 1616519969, -705681347, -372276630,
            1922424092, 1141515625, -1911689386, -1799399087, 1318900467, -1383192650, -230592884, -335329475,
            -1441629429, -538677905, 266344190, -990714718, -545201790, 1477466264, 1268989484, -890272375, -147189626,
            -1298208324, 982702393, -1595305241, -32769654, -1901319538, 1484590115, -1633162495, 1942467223,
            1058352058, 1033496049, -212709592, -739216922, 2067150601, 322542960, -1423026583, 458734153, -1873979479,
            -2108744965, -74416769, 464626817, 1066753135, -980437023, 871973436, -209366992, -1806566176, -1224972457,
            -797940276, -91565135, -1372988358, -583550088, -709968974, 1372140899, -1671225677, -1689287940,
            -305581162, 1356618774, -448492724, -1663569708, -1575621947, -1745624440,
            147059634, -2086572325, -1490122395, 1301890826, 2040537135, 1261550072, -125751850, 1096611573, -892588869,
            196854413, -1676434475, 1718555794, -1475444255, -103184785, 1530052244, -2078148549, -721813867, 486921523,
            -1274936624, -1818105435, 449587716, 470001891, 1350430334, 453927215, -987544614, 1061400037, -1681543270,
            -740884481, 724279309, -315627155, -1264129336, 101119502, 1729348919, 642827279, 917571783, -1991805111,
            747306493, 381545309, -1077733641, 806521069, 285639165, -1837065948, -111531332, -924147071, 969241271,
            448034042, 1763440459, -212213894, 1951141002, -460387004, -1384917466, -2101533988, 848495702, -918196105,
            -1076452627, 1689850363, -1263536158, 961192753, -1331431269, 584927709, 310914602, 1842924227, 1189205699,
            700195886, -1720757325, 2086826235, 1517926122, -1848744429, -1884835454, 1873286742, 1617724710,
            1562440751, 1926379494, -1526594757, -672852952, -272266391, -88582064, -650832619, 1533477097, -1355252381,
            -541434234, 975499848, 1959926488, 2105201314, -1345261014, -1725632085, -1009731117, -2134812511,
            -155657203, 1338794426, -20339884, 2106485915, 30162517, 1447715050, 752122043, 806727619, 1987890698,
            1770008109, -1514561139, 405133353, 1872159796, 1609077829, -906670634, 835081783, -1985138926, 298195466,
            -2109274575, 293306672, 512334423, -1703352083, -758259811, -688037416, 1518317093, -2122802085,
            -1286918510, -1051025860, 155271350, 1216181618, -618367197, -717104513, 715037660, 1697094599, -698423585,
            -1094617089, 245831623, 908748718, -11173440, -1133056151, -466619412, -1444090099, 2039806207, 539219403,
            286983442, 502278961, 56009747, -1993318820, 554653544, 1046391468, 113658445, 101183499, -1577982237,
            321939366, 1221881958, 1790325348, 1972186465, -544648508, -1827564474, 1660388202, 1236924807, 1604830852,
            -819164348, -1521365227, 1682234866, 1562098660, -277831664, -1728099831, 1509378933, -2024369807,
            1179027041, 851334624, -1059325878, 992924109, 1367675132, -1841903078, -1498038901, 368188574, -1685245802,
            1674989369, 1874630087, 995309137, -302067642, -1862953393, -2026754312, 1881734883, 1317698614, 1339598353,
            1629266084, 567186278, -398592512, -1035875218, -1461850061, 574888461, 1223165143, 1323238741, 1575244005,
            -13445324, 219302975, -1745054043, 1287434066, 216958079, -338296868, 375350233, -1119509856, 1639528048,
            -390437796, 840919690, -155152240, 1613633971, -2095387567, 1339226719, -1645666815, 353038895, -360437532,
            2045461970, 864397265, -1948841063, 1414377783, -1428387736, 1866614649, -2107502033, 1924209092,
            -1548149715, 1691270944, 738468456, 251417600, 2106055097, -86202285, 1445708282, -645917304, 1729356539,
            906646052, 2136856722, 2025933506, -25383970, -1481297427, -879320914, -1199665251, 2058011199, 198289895,
            -607799670, -829865969, 104780212, 1970286031, -508115341, 25397940, -1193954407, 1838402557, -1327504794,
            2055969068, 232111061, 1199499189, -920013376, -1191840505, 1856400694, 1558100404, 980744845, 1823954375,
            -764065494, -1685676975, 207880573, 2067840849, -591425643, -906454357, 90578535, -1718181101, -1627267957,
            -1475842652, 1343412690, 1335251533, -563334270, -642054817, 1766672157, -504695410, -1115042115,
            -1537445943, 205214457, -1402614667, 11648468, 2095207736, 1772342452, -343692792, -66178836, 1263651248,
            1241617982, -64777150, 274072168, -314376000, -1547093791, 1108427220, -2127244107, -1039800427, 1161938676,
            1665643042, 1259586880, 26681563, -97987244, 1828140048, 1723707711, -322657661, -865809361, 44274708,
            -310938947, -321524964, -746053322, -2057422336, -1328183136, -469521766, 1545266745, 1936814558,
            -870433796, -364427223, -590871009, 1040790665, -1117778473, -1412775786, 1072038757, -994102562, 72450571,
            -1949992720, -89987353, 1018083562, 1636998845, -2011478343, 1939734705, -736688386, -1791456295,
            -606156291, -2144242805, 450429758, 846986608, 1227399739, -1655133576, 1971805802, -535132953, 1237932458,
            -834643695, 1653512929, 1548690647, -1301031031, 979338843, -2123589878, 1553278795, 1633347891, 918601162,
            1631942883, -1508959736, -1340336037, 85818838, -2002900159 };
    Snake snake;
    Fruit fruit;

    public GameLogic(int frameWidth, int frameHeight) {
        this.frameWidth = frameWidth;
        this.frameHeight = frameHeight;
        this.xVelocity = 0;
        this.yVelocity = -MOVE_AMOUNT;
        this.isMoving = false;
        this.gameOver = false;
        this.random = new Random(69);
        this.highscore = 0;
        this.solved = false;

        // Calculate the initial position of the object in the middle of the frame
        int xHead = innerFrameX + innerFrameWidth / 15 / 2 * 15;
        int yHead = innerFrameY + 270;

        snake = new Snake(xHead, yHead);
        fruit = new Fruit(xHead, yHead);
    }

    public void updateGame() {
        if (gameOver) {
            return;
        }

        if (isMoving) {
            snake.changeDir(xVelocity, yVelocity);
            if (snake.isEat(fruit.getX(), fruit.getY())) {
                snake.eat();
                for (int i = 0; i < encRad95("comp"); i++) {
                    random.nextInt();
                    random.nextInt();
                }
                int fruitX = Math.abs(random.nextInt() % innerFrameWidth);
                int fruitY = Math.abs(random.nextInt() % innerFrameWidth);
                fruit = new Fruit(innerFrameX + fruitX - (fruitX % OBJECT_SIZE),
                        innerFrameY + fruitY - (fruitY % OBJECT_SIZE));
            } else if (snake.isCrash()) {
                gameOver = true;
                isMoving = false;
            } else {
                snake.move();
            }

        }
    }

    public String rad95(int val) {
        String key = "";
        while (val > 0) {
            key = (char) (val % 95 + 32) + key;
            val /= 95;
        }
        return key;
    }

    public int encRad95(String val) {
        int key = 0, exp = 1;
        for (int i = val.length() - 1; i >= 0; i--) {
            key += (val.charAt(i) - 32) * exp;
            exp *= 95;
        }
        return key;
    }

    public void gf() {
        if (!solved) {
            for (int i = 0; i < en.length; i++)
                en[i] ^= random.nextInt();
            solved = true;
        }
    }

    public void df(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setStroke(new BasicStroke(3));
        gf();
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(en));
        Iterator<Integer> it = list.iterator();
        while (it.hasNext()) {
            if (it.next() == 0) {
                g2d.drawLine(it.next(), it.next(),
                        it.next(), it.next());
            } else {
                g2d.drawArc(it.next(), it.next(), it.next(),
                        it.next(), it.next(), it.next());
            }
        }
    }

    public void draw(Graphics g) {
        g.setColor(Color.decode("#212838"));
        g.fillRect(0, 0, frameWidth, frameHeight);

        g.setColor(Color.decode("#61CBFD"));
        g.setFont(new Font("Dialog", Font.PLAIN, 16));
        g.drawString("Score: " + (snake.getScore() < 0 ? 0 : snake.getScore()), innerFrameX - 5, innerFrameY - 30);
        FontMetrics metrics = g.getFontMetrics();
        String high = "Highscore: " + highscore;
        g.drawString(high, innerFrameX + innerFrameWidth + 5 - metrics.stringWidth(high), innerFrameY - 30);
        g.fillRoundRect(innerFrameX - 5, innerFrameY - 5, innerFrameWidth + 10, innerFrameHeight + 10, 5, 5);
        g.fillRoundRect(innerFrameX - 5, innerFrameY - 20, innerFrameWidth + 10, 5, 5, 5);

        for (int x = innerFrameX; x < innerFrameX + innerFrameWidth; x += OBJECT_SIZE) {
            for (int y = innerFrameY; y < innerFrameY + innerFrameHeight; y += OBJECT_SIZE) {
                if ((x + y) / OBJECT_SIZE % 2 == 0) {
                    g.setColor(Color.decode("#202030"));
                } else {
                    g.setColor(Color.decode("#212838"));
                }
                g.fillRect(x, y, OBJECT_SIZE, OBJECT_SIZE);
            }
        }

        if (highscore < snake.getScore())
            highscore = snake.getScore();

        // drawFruit
        if (!(snake.isEat(fruit.getX(), fruit.getY())))
            fruit.draw(g);

        // drawSnake
        snake.draw(g);

        if (gameOver) {
            try {
                InputStream imageStream = SolverGUI.class.getResourceAsStream("/com/images/Ular.png");
                Image image = ImageIO.read(imageStream);
                g.drawImage(image, innerFrameX + 50, innerFrameY + 20, 245, 245, null);
            } catch (IOException e) {
                e.printStackTrace();
            }

            g.setColor(Color.RED);
            g.setFont(new Font("Arial", Font.BOLD, 30));
            metrics = g.getFontMetrics();
            String gameOverText = "GAME OVER";
            int textWidth = metrics.stringWidth(gameOverText);
            int xPosition = innerFrameX + (innerFrameWidth - textWidth) / 2;
            int yPosition = innerFrameY + 300;
            g.drawString(gameOverText, xPosition, yPosition);
            g.setFont(new Font("Dialog", Font.PLAIN, 16));
            metrics = g.getFontMetrics();
            xPosition = innerFrameX + (innerFrameWidth - metrics.stringWidth("click enter to continue!")) / 2;
            g.drawString("click enter to continue!", xPosition, yPosition + 20);

            if (this.rad95(snake.getScore()).equals(key))
                this.df(g);
        }
    }

    public void processKeyPress(int key) {
        if (gameOver) {
            if (key == KeyEvent.VK_ENTER) {
                int xHead = innerFrameX + innerFrameWidth / 15 / 2 * 15;
                int yHead = innerFrameY + 270;
                xVelocity = 0;
                yVelocity = -MOVE_AMOUNT;
                gameOver = false;
                random = new Random(69);
                snake = new Snake(xHead, yHead);
                fruit = new Fruit(xHead, yHead);
            }
        } else {
            if ((key == KeyEvent.VK_LEFT || key == KeyEvent.VK_A) && xVelocity == 0) {
                xVelocity = -MOVE_AMOUNT;
                yVelocity = 0;
            } else if ((key == KeyEvent.VK_RIGHT || key == KeyEvent.VK_D) && xVelocity == 0) {
                xVelocity = MOVE_AMOUNT;
                yVelocity = 0;
            } else if ((key == KeyEvent.VK_UP || key == KeyEvent.VK_W) && yVelocity == 0) {
                xVelocity = 0;
                yVelocity = -MOVE_AMOUNT;
            } else if ((key == KeyEvent.VK_DOWN || key == KeyEvent.VK_S) && yVelocity == 0) {
                xVelocity = 0;
                yVelocity = MOVE_AMOUNT;
            }

            if (!isMoving) {
                isMoving = true;
            }
        }
    }
}

class Coordinate {
    private final int x;
    private final int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}

class Snake implements Drawable {
    private ArrayList<Coordinate> pos;
    private int dirX;
    private int dirY;
    private int len;
    private int score;

    Snake(int x, int y) {
        pos = new ArrayList<Coordinate>();
        len = 5;
        score = -1;
        for (int i = len - 1; i >= 0; i--) {
            pos.add(new Coordinate(x, y + i * MOVE_AMOUNT));
        }
        dirX = 0;
        dirY = -1;
    }

    public void draw(Graphics g) {
        g.setColor(Color.decode("#4FE373"));
        for (Coordinate c : pos)
            g.fillOval(c.getX(), c.getY(), OBJECT_SIZE, OBJECT_SIZE);
        g.setColor(Color.BLACK);
        g.fillOval(pos.get(len - 1).getX() + ((dirX > 0 || dirY > 0) ? 9 : 2),
                pos.get(len - 1).getY() + ((dirX > 0 || dirY > 0) ? 9 : 2), 5, 5);
        g.fillOval(pos.get(len - 1).getX() + ((dirX > 0 || dirY < 0) ? 9 : 2),
                pos.get(len - 1).getY() + ((dirX > 0 || dirY < 0) ? 2 : 9), 5, 5);
    }

    public void changeDir(int x, int y) {
        if (x > 0)
            dirX = 1;
        else if (x < 0)
            dirX = -1;
        else
            dirX = 0;

        if (y > 0)
            dirY = 1;
        else if (y < 0)
            dirY = -1;
        else
            dirY = 0;
    }

    public void move() {
        pos.add(new Coordinate(pos.get(len - 1).getX() + MOVE_AMOUNT * dirX,
                pos.get(len - 1).getY() + MOVE_AMOUNT * dirY));
        pos.remove(0);
    }

    public boolean isCrash() {
        if (pos.get(len - 1).getX() + MOVE_AMOUNT * dirX < innerFrameX
                || pos.get(len - 1).getX() + MOVE_AMOUNT * dirX + OBJECT_SIZE > innerFrameX + innerFrameWidth ||
                pos.get(len - 1).getY() + MOVE_AMOUNT * dirY < innerFrameY
                || pos.get(len - 1).getY() + MOVE_AMOUNT * dirY + OBJECT_SIZE > innerFrameY + innerFrameHeight) {
            return true;
        }

        for (int i = 0; i < len - 1; i++) {
            if (pos.get(i).getX() == pos.get(len - 1).getX() + MOVE_AMOUNT * dirX
                    && pos.get(i).getY() == pos.get(len - 1).getY() + MOVE_AMOUNT * dirY)
                return true;
        }
        return false;
    }

    public boolean isEat(int x, int y) {
        if (pos.get(len - 1).getX() == x && pos.get(len - 1).getY() == y)
            return true;
        return false;
    }

    public int encRad95(String val) {
        int key = 0, exp = 1;
        for (int i = val.length() - 1; i >= 0; i--) {
            key += (val.charAt(i) - 32) * exp;
            exp *= 95;
        }
        return key;
    }

    public void eat() {
        if (score < 0) {
            this.move();
        } else if (len <= 50 && !this.isCrash()) {
            pos.add(new Coordinate(pos.get(len - 1).getX() + MOVE_AMOUNT * dirX,
                    pos.get(len - 1).getY() + MOVE_AMOUNT * dirY));
            len++;
        }
        score = encRad95("comp");
    }

    public int getScore() {
        return score;
    }
}

class Fruit implements Drawable {
    private Coordinate pos;

    Fruit(int x, int y) {
        pos = new Coordinate(x, y);
    }

    public void draw(Graphics g) {
        g.setColor(Color.RED);
        g.fillArc(pos.getX(), pos.getY(), OBJECT_SIZE, OBJECT_SIZE * 4 / 5, 0, 360);
        g.fillArc(pos.getX(), pos.getY() + 5, OBJECT_SIZE / 3, OBJECT_SIZE * 2 / 3, 0, 360);
        g.fillArc(pos.getX() + 10, pos.getY() + 5, OBJECT_SIZE / 3, OBJECT_SIZE * 2 / 3, 0, 360);
        g.setColor(Color.WHITE);
        g.fillArc(pos.getX() + 5, pos.getY() + 3, OBJECT_SIZE * 2 / 3, OBJECT_SIZE / 3, 0, 360);
    }

    public int getX() {
        return pos.getX();
    }

    public int getY() {
        return pos.getY();
    }
}