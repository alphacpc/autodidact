class Person{
  String fname;
  String lname;
  String sexe;
  int age;

  Person(this.fname, this.lname, this.sexe, this.age);


  whoIam(){
    print("Je m'appelle $fname $lname de sexe $sexe et age de $age ans.");
  }


}

void main(){


  Person person1 = Person('Alpha','DIALLO','Masculin', 25);
  Person person2 = Person('Awa', 'DIALLO', 'Féminin', 7);

  person2.whoIam();
  person1.whoIam();



}