public static void main(String[]args){
    TryWithResourceDemo demo=new TryWithResourceDemo();

    try(demo){
        demo.doSomething();
    }
}
