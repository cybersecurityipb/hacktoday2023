use std::{io::{self, Write}, process::exit};

struct User {
    username: String,
    password: String,
    secret : String,
}

fn add_user(username: String, password: String) -> User {
    User {
        username,
        password,
        secret: String::from("NBQWG23UN5SGC6L3JVZEW4TBMJZXG4YK"), // hacktoday{MrKrabsss (part 1/2)
    }
}

fn register() -> User{
    println!("[+] Register");

    print!("Username : ");
    io::stdout().flush().unwrap();
    let mut username = String::new();

    io::stdin()
        .read_line(&mut username)
        .expect("Input Failed!");

    print!("Password : ");
    io::stdout().flush().unwrap();
    let mut password = String::new();

    io::stdin()
        .read_line(&mut password)
        .expect("Input Failed!");

    add_user(username, password)

}

fn login(users:&Vec<User>) -> bool {
    println!("[+] Login");

    print!("Username : ");
    io::stdout().flush().unwrap();
    let mut username = String::new();

    io::stdin()
        .read_line(&mut username)
        .expect("Input Failed!");

    print!("Password : ");
    io::stdout().flush().unwrap();
    let mut password = String::new();

    io::stdin()
        .read_line(&mut password)
        .expect("Input Failed!");

    if users.iter().any(|user| user.username == username && user.password == password){
        if username.trim().eq("ru5t0n0") && password.trim().eq("hektod23"){
            let flag = String::from("_is_Rustaceans}");
            println!("part 2/2 sir ._. : {}", flag);
            return true
        } else {
            println!("Login, but for what??");
            return true
        }
    } 

    false

}

fn main() {

    let mut users: Vec<User> = Vec::new();

    println!("=====================");
    println!("Welcome to my machine");
    println!("=====================");

    loop {
        println!("[1] Register");
        println!("[2] Login");
        println!("[3] Exit");

        print!("> ");
        io::stdout().flush().unwrap();

        let mut input = String::new();

        io::stdin()
            .read_line(&mut input)
            .expect("[!] Input Failed!");

        let input: u32 = match input.trim().parse(){
            Ok(num) => match num{
                1 => num,
                2 => num,
                3 => {
                    println!("[!] Program Exit!");
                    exit(0)
                },
                _ => {
                    println!("[!] Not on menu!");
                    continue;
                }
            },
            Err(_) => {
                println!("[!] number please");
                exit(1);
            }
        };

        if input == 1{
            let account: User = register();
            users.push(account);
            println!("[!] User registered successfully!");
        }
        else{
            if login(&users){
                break;
            } else{
                println!("[!] Please register first!")
            }
        }
    }
}