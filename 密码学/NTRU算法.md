##  求多项式 poly 与 x^N-1 的最大公约数

```java 
public static int gcdPoly(int N, int m, int[] poly, int[] result){
  int[] originPoly = new int[N+1];
  System.arraycopy(poly, 0, originPoly, 0, poly.length);
  Tools.polyAddDig(poly, m, poly, m);     // 将多项式中的负数变为正数

  int[] numPoly = new int[N+1];       // x的n次方 -1

  /* 赋值，初始化 */
  numPoly[N] = 1;
  numPoly[0] = -1;
  Tools.polyAddDig(numPoly, m, numPoly, m);

  int[] divPoly = new int[N+1];       // 被除数多项式
  int[] remaPoly = new int[N+1];      // 余数多项式
  int[] gcdPoly = new int[N+1];       // 最大公因数多项式
  int[] flagPoly = new int[N+1];      // 判断多项式，用于终止循环,初始值为0
  int[] tempPolyResult = new int[N+1];    // 中间值
  int[] tempPolyRema = new int[N+1];      // 中间值

  divPoly = poly.clone();
  Tools.polyDivPoly(N, m, numPoly, poly, tempPolyResult, remaPoly);


  /* 求最大公因数 */
  while( !Arrays.equals(remaPoly,flagPoly) ){
    Tools.initPolynomial(tempPolyResult);
    Tools.polyDivPoly(N, m, divPoly, remaPoly, tempPolyResult, tempPolyRema);
    //            divPoly = remaPoly.clone();
    //            remaPoly = tempPolyRema.clone();

    System.arraycopy(remaPoly, 0, divPoly, 0, remaPoly.length);
    System.arraycopy(tempPolyRema, 0, remaPoly, 0, tempPolyRema.length);

    Tools.initPolynomial(tempPolyResult);   // 清空
    Tools.initPolynomial(tempPolyResult);   // 清空
  }

  System.arraycopy(divPoly, 0, result, 0, divPoly.length);

  System.arraycopy(originPoly, 0, poly, 0, originPoly.length);    // 将多项式还原

  return 0;
}
```

##  数求逆元

```java
public static long digRev(long a, long m) throws IllegalArgumentException {
  long div = m;   // 被除数
  long rema = a % m; // 余数
  long temp = 0;      //
  long gcd = 0;        // 最大公因数
  ArrayList<Long> divList = new ArrayList<Long>();
  ArrayList<Long> remaList = new ArrayList<Long>();

  divList.add(a);
  remaList.add(m);

  while( rema!=0 ){
    divList.add(div);
    remaList.add(rema);
    temp = div % rema;
    div = rema;
    rema = temp;
  }

  gcd = div;
  if( gcd!=1 ){
    return -1;
  }


  int i = divList.size()-2;
  long inv_a = 1;
  long inv_b = -divList.get(i) / remaList.get(i);
  for(i = i-1; i>=0; i--){
    temp = inv_a;
    inv_a = inv_b;
    inv_b = temp - (divList.get(i) / remaList.get(i)) * inv_b;
  }

  if( inv_a < 0 )
    inv_a = inv_a + m;

  return inv_a;
}
```

##  解一次同余方程

```java
public static long[] sovleFun(long a, long b, long m){
  long d = Tools.gcd(a, m);

  if( b % d != 0 ){       // 判断是否有解
    //            System.out.println("错误：solveFun");
    return new long[]{0};
  }

  long af = a / d;
  long mf = m / d;
  long x0 = Tools.digRev(af, mf);
  long x = (b / d * x0) % (m / d);
  long[] xList = new long[(int) (d)];

  for(int i=0; i<d; i++){
    xList[i] = (x + mf * i) % m;
  }

  return xList;
}
```

##  求多项式的逆元

```java
public static int polyRev(int N, int m, int[] polynomial, int[] result){
  int[] numPoly = new int[N+1];       // x的n次方 -1

  /* 赋值，初始化 */
  numPoly[N] = 1;
  numPoly[0] = -1;
  Tools.polyAddDig(numPoly, m, numPoly, m);

  int k = 1;      // 求最大公因数(常数项)与m的逆元
  int[] divPoly = new int[N+1];       // 被除数多项式
  int[] remaPoly = new int[N+1];      // 余数多项式
  int[] gcdPoly = new int[N+1];       // 最大公因数多项式
  int[] flagPoly = new int[N+1];      // 判断多项式，用于终止循环,初始值为0
  int[] tempPolyResult = new int[N+1];    // 中间值
  int[] tempPolyRema = new int[N+1];      // 中间值
  int[] tempPolyDiv = new int[N+1];       // 中间值
  ArrayList<int[]> divPolyList = new ArrayList<int[]>();      // 被除数多项式集合
  ArrayList<int[]> remaPolyList = new ArrayList<int[]>();     // 余数多项式集合

  gcdPoly(N, m, polynomial, gcdPoly);      // 求最大公约数
  flagPoly[0] = gcdPoly[0];

  /* 判断是否有解，如果最大公因数为一个常数，就有解，否则无解 */
  if( !Arrays.equals(gcdPoly, flagPoly) ) {
    //            System.out.println("错误：polyRev");
    return -1;
  }

  /* 判断最大公因数是否是1(此时的最大公因数应该是一个常数) */
  flagPoly[0] = 1;
  if( !Arrays.equals(gcdPoly, flagPoly) ) {   // 不是 1
    k = (int) digRev(gcdPoly[0], m);        // 求最大公因数(常数项)与m的逆元
    polyMulDig(polynomial, k, tempPolyResult, m);
    polynomial = tempPolyResult.clone();
    initPolynomial(tempPolyResult);
  }

  initPolynomial(flagPoly);   // 将 flagPoly 置为0

  /* 将 X^N-1 与 poly 加入到数列中 */
  divPolyList.add(numPoly);
  remaPolyList.add(polynomial);

  System.arraycopy(polynomial, 0, divPoly, 0, polynomial.length);
  if(Tools.polyDivPoly(N, m, numPoly, polynomial, tempPolyResult, remaPoly) == -1){
    System.exit(0);
  }


  /* 求最大公因数，并保存除数和余数 */
  while( !Arrays.equals(remaPoly,flagPoly) ){
    divPolyList.add(divPoly);
    remaPolyList.add(remaPoly);

    Tools.initPolynomial(tempPolyResult);
    if(Tools.polyDivPoly(N, m, divPoly, remaPoly, tempPolyResult, tempPolyRema) == -1){
      System.out.println("polyRev");
      System.exit(0);
    }
    divPoly = remaPoly.clone();
    remaPoly = tempPolyRema.clone();

    Tools.initPolynomial(tempPolyResult);   // 清空
    Tools.initPolynomial(tempPolyResult);   // 清空
  }

  gcdPoly = divPoly.clone();      // 此时的最大公因数应该是 1

  int i = divPolyList.size() - 2;
  int[] inv_aPoly = gcdPoly.clone();
  int[] inv_bPoly = new int[N+1];
  if(Tools.polyDivPoly(N, m, divPolyList.get(i), remaPolyList.get(i), inv_bPoly, tempPolyResult) == -1){
    System.out.println("polyRev");
    System.exit(0);
  }
  Tools.polyMulDig(inv_bPoly, -1, inv_bPoly, m);

  for(i = i-1; i>=0; i--){
    Tools.initPolynomial(tempPolyDiv);
    Tools.initPolynomial(tempPolyRema);

    tempPolyResult = inv_aPoly.clone();
    inv_aPoly = inv_bPoly.clone();
    if(Tools.polyDivPoly(N, m, divPolyList.get(i), remaPolyList.get(i), tempPolyDiv, tempPolyRema) == -1){
      System.out.println("polyRev");
      System.exit(0);
    }
    Tools.initPolynomial(tempPolyRema);
    Tools.polyMulPoly(N, m, tempPolyDiv, inv_bPoly, tempPolyRema);
    Tools.polyMulDig(tempPolyRema, -1, tempPolyRema, m);
    Tools.initPolynomial(inv_bPoly);
    Tools.polyAddPoly(N, m, tempPolyResult, tempPolyRema, inv_bPoly);
  }


  for(int as=0; as<inv_bPoly.length; as++)
    result[as] = (inv_bPoly[as] * k) % m;

  return 0;
}
```



##  部分代码

以下方法是实现NTRU算法的关键方法。

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Tools {

    /**
     * 求最大公约数
     * @author 白生
     * @date 2024/1/19 22:07
     */
    public static long gcd(long num1, long num2){
        long divisor = num2;   // 除数
        long remainder = num1 % num2; // 余数
        long temp = 0;

        while( remainder!=0 ){
            temp = divisor % remainder;
            divisor = remainder;
            remainder = temp;
        }

        return divisor;
    }


    /**
     * 求多项式 poly 与 x^N-1 的最大公约数
     * @author 白生
     * @date 2024/1/24 19:36
     */
    public static int gcdPoly(int N, int m, int[] poly, int[] result){
        int[] originPoly = new int[N+1];
        System.arraycopy(poly, 0, originPoly, 0, poly.length);
        Tools.polyAddDig(poly, m, poly, m);     // 将多项式中的负数变为正数

        int[] numPoly = new int[N+1];       // x的n次方 -1

        /* 赋值，初始化 */
        numPoly[N] = 1;
        numPoly[0] = -1;
        Tools.polyAddDig(numPoly, m, numPoly, m);

        int[] divPoly = new int[N+1];       // 被除数多项式
        int[] remaPoly = new int[N+1];      // 余数多项式
        int[] gcdPoly = new int[N+1];       // 最大公因数多项式
        int[] flagPoly = new int[N+1];      // 判断多项式，用于终止循环,初始值为0
        int[] tempPolyResult = new int[N+1];    // 中间值
        int[] tempPolyRema = new int[N+1];      // 中间值

        divPoly = poly.clone();
        Tools.polyDivPoly(N, m, numPoly, poly, tempPolyResult, remaPoly);


        /* 求最大公因数 */
        while( !Arrays.equals(remaPoly,flagPoly) ){
            Tools.initPolynomial(tempPolyResult);
            Tools.polyDivPoly(N, m, divPoly, remaPoly, tempPolyResult, tempPolyRema);
//            divPoly = remaPoly.clone();
//            remaPoly = tempPolyRema.clone();

            System.arraycopy(remaPoly, 0, divPoly, 0, remaPoly.length);
            System.arraycopy(tempPolyRema, 0, remaPoly, 0, tempPolyRema.length);

            Tools.initPolynomial(tempPolyResult);   // 清空
            Tools.initPolynomial(tempPolyResult);   // 清空
        }

        System.arraycopy(divPoly, 0, result, 0, divPoly.length);

        System.arraycopy(originPoly, 0, poly, 0, originPoly.length);    // 将多项式还原

        return 0;
    }


    /**
     * 数求逆元
     * ax = 1 (mod m)
     * @author 白生
     * @date 2024/1/20 16:15
     */
    public static long digRev(long a, long m) throws IllegalArgumentException {
        long div = m;   // 被除数
        long rema = a % m; // 余数
        long temp = 0;      //
        long gcd = 0;        // 最大公因数
        ArrayList<Long> divList = new ArrayList<Long>();
        ArrayList<Long> remaList = new ArrayList<Long>();

        divList.add(a);
        remaList.add(m);

        while( rema!=0 ){
            divList.add(div);
            remaList.add(rema);
            temp = div % rema;
            div = rema;
            rema = temp;
        }

        gcd = div;
        if( gcd!=1 ){
            return -1;
        }


        int i = divList.size()-2;
        long inv_a = 1;
        long inv_b = -divList.get(i) / remaList.get(i);
        for(i = i-1; i>=0; i--){
            temp = inv_a;
            inv_a = inv_b;
            inv_b = temp - (divList.get(i) / remaList.get(i)) * inv_b;
        }

        if( inv_a < 0 )
            inv_a = inv_a + m;

        return inv_a;
    }


    /**
     * 解一次同余方程
     * ax = b (mod m)
     * @author 白生
     * @date 2024/1/20 20:40
     */
    public static long[] sovleFun(long a, long b, long m){
        long d = Tools.gcd(a, m);

        if( b % d != 0 ){       // 判断是否有解
//            System.out.println("错误：solveFun");
            return new long[]{0};
        }

        long af = a / d;
        long mf = m / d;
        long x0 = Tools.digRev(af, mf);
        long x = (b / d * x0) % (m / d);
        long[] xList = new long[(int) (d)];

        for(int i=0; i<d; i++){
            xList[i] = (x + mf * i) % m;
        }

        return xList;
    }


    /**
     * 多项式加多项式
     * @author 白生
     * @date 2024/1/19 22:16
     */
    public static void polyAddPoly(int N, int m, int[] polynomialA, int[] polynomialB, int[] result){
        int factor = 0;  // 系数

        for(int i=0; i<polynomialA.length; i++){
            factor = polynomialA[i] + polynomialB[i];
            result[i] = factor % m;
        }
    }


    /**
     * 多项式减多项式
     * @author 白生
     * @date 2024/1/19 22:16
     */
    public static void polySubPoly(int N, int m, int[] polynomialA, int[] polynomialB, int[] result){
        int factor = 0;  // 系数

        for(int i=0; i<polynomialA.length; i++){
            factor = polynomialA[i] - polynomialB[i] + m;
            result[i] = factor % m;
        }
    }


    /**
     * 多项式乘多项式
     * @author 白生
     * @date 2024/1/19 21:24
     */
    public static void polyMulPoly(int N, int m, int[] polynomialA, int[] polynomialB, int[] result){    // N为参数N，m为模数， 后两个参数为多项式
        int factor = 0, exponents = 0;  // 系数、指数

        for(int i=0; i<polynomialA.length; i++){
            if( polynomialA[i]!=0 ){
                for(int j=0; j<polynomialB.length; j++){
                    if( polynomialB[j]!=0 ){
                        factor = polynomialA[i] * polynomialB[j] % m;
                        exponents = (i + j);
                        result[exponents] = (result[exponents] + factor) % m;
                    }
                }
            }

        }

    }


    /**
     * 多项式乘多项式,次数模N
     * @author 白生
     * @date 2024/1/19 21:24
     */
    public static void polyMulPolyModN(int N, int m, int[] polynomialA, int[] polynomialB, int[] result){    // N为参数N，m为模数， 后两个参数为多项式
        int factor = 0, exponents = 0;  // 系数、指数

        for(int i=0; i<polynomialA.length; i++){
            if( polynomialA[i]!=0 ){
                for(int j=0; j<polynomialB.length; j++){
                    if( polynomialB[j]!=0 ){
                        factor = polynomialA[i] * polynomialB[j] % m;
                        exponents = (i + j) % N;
                        result[exponents] = (result[exponents] + factor + m) % m;
                    }
                }
            }

        }

    }


    /**
     * 多项式除多项式
     * @author 白生
     * @date 2024/1/19 22:53
     */
    public static int polyDivPoly(int N, int m, int[] polynomialA, int[] polynomialB, int[] result, int[] remainder){
        int factor = 0, exponents = 0;  // 系数、指数
        int i = polynomialA.length-1, j = polynomialB.length - 1;
        int[] tempResult = new int[N+1];
        int[] tempPolyB = new int[N+1];
        Tools.initPolynomial(tempResult);
        Tools.initPolynomial(tempPolyB);

        /* 找到polynomialB的最高次项 */
        for(; j>=0; j--){
            if( polynomialB[j]!=0 )
                break;
        }

        for(; i>=0; i--) {
            if (polynomialA[i] != 0) {
                Tools.initPolynomial(tempResult);
                Tools.initPolynomial(tempPolyB);

                /* i<j */
                if (i < j)
                    break;


                /* i>j */
                if (i > j) {
                    int[] tempMUlPoly = new int[N + 1];
                    Tools.initPolynomial(tempMUlPoly);      // 初始化，令值为0
                    tempMUlPoly[i - j] = 1;
                    Tools.polyMulPoly(N, m, polynomialB, tempMUlPoly, tempPolyB);   // tempPolyB 为升了次后的被除数

                    if (polynomialA[i] == polynomialB[j]) {
                        Tools.polySubPoly(N, m, polynomialA, tempPolyB, tempResult);
                        result[i - j] = 1;
                        polynomialA = tempResult.clone();       // 深拷贝
                    } else if (polynomialA[i] % polynomialB[j] == 0) {
                        int k = polynomialA[i] / polynomialB[j];    // k为倍数
                        result[i - j] = k;
                        Tools.polyMulDig(tempPolyB, k, tempPolyB, m);
                        Tools.polySubPoly(N, m, polynomialA, tempPolyB, tempResult);
                        polynomialA = tempResult.clone();       // 深拷贝
                    } else {
                        int k = (int) Tools.sovleFun(polynomialB[j], polynomialA[i], m)[0];
                        if( k == 0 ) {
//                            System.out.println("错误：polyDivPoly");
                            return -1;
                        }
                        result[i - j] = k;
                        Tools.polyMulDig(tempPolyB, k, tempPolyB, m);
                        Tools.polySubPoly(N, m, polynomialA, tempPolyB, tempResult);
                        polynomialA = tempResult.clone();       // 深拷贝
                    }
                }


                /* 以下认为 i==j,即两个多项式最高阶相等 */
                if (i == j) {
                    if (polynomialA[i] == polynomialB[j]) {
                        Tools.polySubPoly(N, m, polynomialA, polynomialB, tempResult);
                        result[i - j] = 1;
                        polynomialA = tempResult.clone();       // 深拷贝
                    } else if (polynomialA[i] % polynomialB[j] == 0) {
                        int k = polynomialA[i] / polynomialB[j];    // k为倍数
                        result[i - j] = k;
                        Tools.polyMulDig(polynomialB, k, tempPolyB, m);
                        Tools.polySubPoly(N, m, polynomialA, tempPolyB, tempResult);
                        polynomialA = tempResult.clone();       // 深拷贝
                    } else {
                        int k = (int) Tools.sovleFun(polynomialB[j], polynomialA[i], m)[0];
                        if( k == 0 ) {
//                            System.out.println("错误：polyDivPoly");
                            return -1;
                        }
                        result[i - j] = k;
                        Tools.polyMulDig(polynomialB, k, tempPolyB, m);
                        Tools.polySubPoly(N, m, polynomialA, tempPolyB, tempResult);
                        polynomialA = tempResult.clone();       // 深拷贝
                    }
                }
            }
        }
//        r = polynomialA.clone();      // 为什么用这句代码函数返回后r的值为空？

        /* r为余数 */
        for(i=0; i<polynomialA.length; i++)
            remainder[i] = polynomialA[i];

        return 0;
    }


    /**
     * 多项式系数同时加一个数(模m)
     * @author 白生
     * @date 2024/1/20 11:24
     */
    public static void polyAddDig(int[] poly, int dig, int[] result, int m){
        for(int i=0; i<poly.length; i++){
            if( poly[i]!=0 ){
                result[i] = (poly[i] + dig) % m;
                if( result[i] < 0 )
                    result[i] = (result[i] + m) % m;
            }
        }
    }


    /**
     * 多项式系数同时乘一个数（模 m）
     * @author 白生
     * @date 2024/1/20 11:25
     */
    public static void polyMulDig(int[] poly, int dig, int[] result, int m){
        for(int i=0; i<poly.length; i++){
            if( poly[i]!=0 )
                result[i] = (poly[i] * dig + m) % m;
        }
    }


    /**
     * 初始化多项式，默认设置为0
     * @author 白生
     * @date 2024/1/19 21:12
     */
    public static void initPolynomial(int[] polynomial){
        Arrays.fill(polynomial, 0);
    }


    /**
     * 求多项式的逆元
     * @author 白生
     * @date 2024/1/24 19:19
     */
    public static int polyRev(int N, int m, int[] polynomial, int[] result){
        int[] numPoly = new int[N+1];       // x的n次方 -1

        /* 赋值，初始化 */
        numPoly[N] = 1;
        numPoly[0] = -1;
        Tools.polyAddDig(numPoly, m, numPoly, m);

        int k = 1;      // 求最大公因数(常数项)与m的逆元
        int[] divPoly = new int[N+1];       // 被除数多项式
        int[] remaPoly = new int[N+1];      // 余数多项式
        int[] gcdPoly = new int[N+1];       // 最大公因数多项式
        int[] flagPoly = new int[N+1];      // 判断多项式，用于终止循环,初始值为0
        int[] tempPolyResult = new int[N+1];    // 中间值
        int[] tempPolyRema = new int[N+1];      // 中间值
        int[] tempPolyDiv = new int[N+1];       // 中间值
        ArrayList<int[]> divPolyList = new ArrayList<int[]>();      // 被除数多项式集合
        ArrayList<int[]> remaPolyList = new ArrayList<int[]>();     // 余数多项式集合

        gcdPoly(N, m, polynomial, gcdPoly);      // 求最大公约数
        flagPoly[0] = gcdPoly[0];

        /* 判断是否有解，如果最大公因数为一个常数，就有解，否则无解 */
        if( !Arrays.equals(gcdPoly, flagPoly) ) {
//            System.out.println("错误：polyRev");
            return -1;
        }

        /* 判断最大公因数是否是1(此时的最大公因数应该是一个常数) */
        flagPoly[0] = 1;
        if( !Arrays.equals(gcdPoly, flagPoly) ) {   // 不是 1
            k = (int) digRev(gcdPoly[0], m);        // 求最大公因数(常数项)与m的逆元
            polyMulDig(polynomial, k, tempPolyResult, m);
            polynomial = tempPolyResult.clone();
            initPolynomial(tempPolyResult);
        }

        initPolynomial(flagPoly);   // 将 flagPoly 置为0

        /* 将 X^N-1 与 poly 加入到数列中 */
        divPolyList.add(numPoly);
        remaPolyList.add(polynomial);

        System.arraycopy(polynomial, 0, divPoly, 0, polynomial.length);
        if(Tools.polyDivPoly(N, m, numPoly, polynomial, tempPolyResult, remaPoly) == -1){
            System.exit(0);
        }


        /* 求最大公因数，并保存除数和余数 */
        while( !Arrays.equals(remaPoly,flagPoly) ){
            divPolyList.add(divPoly);
            remaPolyList.add(remaPoly);

            Tools.initPolynomial(tempPolyResult);
            if(Tools.polyDivPoly(N, m, divPoly, remaPoly, tempPolyResult, tempPolyRema) == -1){
                System.out.println("polyRev");
                System.exit(0);
            }
            divPoly = remaPoly.clone();
            remaPoly = tempPolyRema.clone();

            Tools.initPolynomial(tempPolyResult);   // 清空
            Tools.initPolynomial(tempPolyResult);   // 清空
        }

        gcdPoly = divPoly.clone();      // 此时的最大公因数应该是 1

        int i = divPolyList.size() - 2;
        int[] inv_aPoly = gcdPoly.clone();
        int[] inv_bPoly = new int[N+1];
        if(Tools.polyDivPoly(N, m, divPolyList.get(i), remaPolyList.get(i), inv_bPoly, tempPolyResult) == -1){
            System.out.println("polyRev");
            System.exit(0);
        }
        Tools.polyMulDig(inv_bPoly, -1, inv_bPoly, m);

        for(i = i-1; i>=0; i--){
            Tools.initPolynomial(tempPolyDiv);
            Tools.initPolynomial(tempPolyRema);

            tempPolyResult = inv_aPoly.clone();
            inv_aPoly = inv_bPoly.clone();
            if(Tools.polyDivPoly(N, m, divPolyList.get(i), remaPolyList.get(i), tempPolyDiv, tempPolyRema) == -1){
                System.out.println("polyRev");
                System.exit(0);
            }
            Tools.initPolynomial(tempPolyRema);
            Tools.polyMulPoly(N, m, tempPolyDiv, inv_bPoly, tempPolyRema);
            Tools.polyMulDig(tempPolyRema, -1, tempPolyRema, m);
            Tools.initPolynomial(inv_bPoly);
            Tools.polyAddPoly(N, m, tempPolyResult, tempPolyRema, inv_bPoly);
        }


        for(int as=0; as<inv_bPoly.length; as++)
            result[as] = (inv_bPoly[as] * k) % m;

        return 0;
    }


    /**
     * center-lift 操作
     * @author 白生
     * @date 2024/1/25 20:27
     */
    public static int centerLeft(int[] poly, int m){
        int limit = m / 2;

        for(int i=0; i<poly.length; i++){
            if( poly[i] > limit )
                poly[i] = poly[i] - m;
            if( poly[i] < -limit )
                poly[i] = poly[i] + m;
        }

        return 0;
    }


    /**
     * 检查 fx 对于模 m 是否有逆元
     * @author 白生
     * @date 2024/2/3 11:03
     */
    public static boolean checkFx(int N, int p, int q, int[] fx){

        int[] Fp = new int[N+1];
        int[] Fq = new int[N+1];

        if(Tools.polyRev(N, p, fx, Fp) == -1)
            return false;
        if(Tools.polyRev(N, q, fx, Fq) == -1)
            return false;

        int[] flag = new int[N+1];
        flag[0] = 1;

        int[] s = new int[N+1];
        int[] r = new int[N+1];

        Tools.polyMulPolyModN(N, p, fx, Fp, s);
        Tools.polyMulPolyModN(N, q, fx, Fq, r);

        if( !Arrays.equals(s,flag) )
            return false;
        if( !Arrays.equals(r, flag) )
            return false;

        return true;
    }
}
```

