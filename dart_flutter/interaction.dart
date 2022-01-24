import 'dart:io';

void main(){

  stdout.write("Votre prenom : ");
  var fname = stdin.readLineSync();

  stdout.write("Votre nom de famille : ");
  var lname = stdin.readLineSync();

  stdout.write("Ton age : ");
  var age = stdin.readLineSync();
  int? age_convert = int.parse('$age');

  print("Je m'appelle $fname $lname et j'ai $age ans.");


  if(age_convert < 18){
    print("Je suis mineur");
  }else{
    print("Je suis majeur");
  }


}