#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <conio.h>

using namespace std;
string cutZeros (string s){
    string o;
    bool flag =0;
    int i=0;
    if(atoi(s.c_str())==0) return o;
    while(!flag){
        if(s[i]=='1'){
            flag=1;
            o=s.substr(i,(s.length()-i));
        }
        i++;
    }
    return o;
}

string concatinateZeros(string s, int length){
    string o="";
    int remainingLength=length-s.length();
    for (int i =0; i<remainingLength; i++){
        o+='0';
    }
    o+=s;


    return o;
}

string Generator(string msgTmp,string kTmp){
    string temp;

    char * End;
    string intermediateMsg;

    int inputMsgLength=msgTmp.length();

    int kLength=kTmp.length();
    int shiftBits = kTmp.length()-1;

    int dividedBitsCount=0;
    string dividedBits="";
    string product="";
    string concatinatedMsg=msgTmp+concatinateZeros("",shiftBits);
    int value;
    for (int i =0; i<(inputMsgLength+shiftBits);i++){
        dividedBits+=concatinatedMsg[i];
        dividedBitsCount++;
        if(dividedBitsCount==kLength){
            value = (((int) strtol(dividedBits.c_str(),& End, 2))^ ((int) strtol(kTmp.c_str(),& End, 2)));
            dividedBits=cutZeros( bitset<64>(value).to_string());
            dividedBitsCount=dividedBits.length();
            product+='1';
        }
        else{
            product+='0';
        }


    }
    intermediateMsg=msgTmp+concatinateZeros(dividedBits,shiftBits);
    return intermediateMsg;
}

void Verifier(string imMsg,string k){
    bool correct=0;
    char * End;

    int dividedBitsCount=0;
    string dividedBits="";
    string product="";
    int value;
    for (int i =0; i<(imMsg.length());i++){
        dividedBits+=imMsg[i];
        dividedBitsCount++;
        if(dividedBitsCount==k.length()){
            value = (((int) strtol(dividedBits.c_str(),& End, 2))^ ((int) strtol(k.c_str(),& End, 2)));
            dividedBits=cutZeros( bitset<64>(value).to_string());
            dividedBitsCount=dividedBits.length();
            product+='1';
        }
        else{
            product+='0';
        }
    }
    if (atoi(dividedBits.c_str())==0){correct=1;}

    if(correct)cout<<"\nVerifier output: msg is correct";
    else cout<<"\nVerifier output: msg is Not correct";

}

string Alter (string Msg,int bitNumber){
    string alteredMsg=Msg;

    if(alteredMsg[bitNumber-1]=='0')   alteredMsg[bitNumber-1]='1';
    else alteredMsg[bitNumber-1]='0';
    cout << "\naltered msg "<<alteredMsg;
    return alteredMsg;
}

int main()
{
    char choice='c';
    string msgTmp,kTmp;
    string intermediateMsg;
    int bitNumber;
    while (choice=='c'){
        cout<<"\nPlease Enter the m-bit msg: ";
        cin>>msgTmp;

        cout<<"\nPlease Enter the K-bit Polynomial: ";
        cin>>kTmp;
        intermediateMsg=Generator( msgTmp,kTmp);

        cout<<"\nThe generate output is "<<intermediateMsg;

        cout<<"\nDo you want to alter the msg before verifying? press y or n";
        if(_getch()== 'y'){
            cout<< "\nPlease Enter the number of the Bit you wanna change: ";
            cin>> bitNumber;
            Verifier(Alter(intermediateMsg,bitNumber),kTmp);
        }
        else{
            Verifier(intermediateMsg,kTmp);
        }


        cout<<"\nDo you want to send another msg? if yes press c if not press q";
        choice=_getch();

    }


    return 0;
}
