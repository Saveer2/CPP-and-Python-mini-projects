#include <iostream>
#include <string>
using namespace std;

class ExpenseTracker {
private :
	double totalfood = 0.0, totaltransport = 0.0, totalother = 0.0, totalexpenses = 0.0;
	
public :
	void add_expense(){
		int choice;
		double amount;
		
		cout<<"** Choose Any Expense category : \n1. Food \n2. Transport \n3. Other"<<endl;
		cout<<"** Enter Your Choice : ";
		cin>>choice;
		cout<<" "<<endl;
		if(choice<1 || choice>3){
			cout<<"You have entered a invalid category!!"<<endl;
			return;
		}
		else{
			cout<<"Enter Amount : ";
			cin>>amount;
			cout<<" "<<endl;
		
			if(choice == 1){
				totalfood += amount;
			}
			else if(choice == 2){
				totaltransport += amount;	
			}
			else if(choice == 3){
				totalother += amount;
			}
			totalexpenses += amount;
			cout<<"** Expense Added Successfully!!"<<"\n\n\n\n"<<endl;	
		}
	}
	void view_expense(){
		if(totalexpenses == 0){
			cout<<"** No expenses recorded!! \n"<<endl;
			return;
		}
		cout<<"** ALL EXPENSES **\n"<<endl;
		cout<<"* Food : $"<<totalfood<<endl;
		cout<<"* Transport : $"<<totaltransport<<endl;
		cout<<"* Other : $"<<totalother<<"\n\n\n\n"<<endl;
	}
	void analyze_expense(){
		if(totalexpenses == 0){
			cout<<"** No expenses recorded!! "<<endl;
			return;
		}
		cout<<"**  Analyze Expenses  **\n"<<endl;
		cout<<"* Total Expenses : $"<<totalexpenses<<endl;
		double foodpercentage = (totalfood / totalexpenses)*100;
		if(totalfood>0){
			cout<<"Food : $"<<totalfood<<" ("<<foodpercentage<<"%)"<<endl;
		}
		double transportpercentage = (totaltransport / totalexpenses)*100;
		if(totaltransport>0){
			cout<<"Transport : $"<<totaltransport<<" ("<<transportpercentage<<"%)"<<endl;
		}
		double otherpercentage = (totalother / totalexpenses)*100;
		if(totalother>0){
			cout<<"Other : $"<<totalother<<" ("<<otherpercentage<<"%)"<<endl;
		}
		cout<<"\n\n\n\n";	
	}
};

int main(){
	ExpenseTracker E1;
	int choice;
	do{	
		cout<<"------------------------------------------"<<endl;
		cout<<"|  ****  Personal Expense Tracker  ****  |"<<endl;
		cout<<"------------------------------------------"<<endl;
	
		cout<<"1. Add Expense \n2. View Expenses \n3. Analyze Expenses \n4. Exit"<<endl;
		cout<<"* Enter your Choice : ";
		cin>>choice;
		cout<<" "<<endl;
	
		switch(choice){
			case 1 :
				E1.add_expense();
				break;
			case 2 :
				E1.view_expense();
				break;
			case 3 :
				E1.analyze_expense();
				break;
			case 4 :
				cout<<"**  Exiting the program...  **"<<endl;
				cout<<" "<<endl;
				cout<<"-----------------------------------------------------------"<<endl;
				cout<<"|  **  THank You For Using Personal Expense Tracker!! **  |"<<endl;
				cout<<"-----------------------------------------------------------"<<endl;
				break;
			default:
				cout<<"Invalid Choice!!"<<endl;	
		}
	}
	while (choice != 4);
	return 0;
}