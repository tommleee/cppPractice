class Vehicle
{
public:
void buy();
void register(string registration_no);
void sell();
string get_registration_no() const;
private:
string registration_no;
};