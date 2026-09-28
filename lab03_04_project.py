"""
Mã sinh viên: 202418859
Họ tên: Lê Hùng Cường
Lab 03-04 - Overloading
 Chương trình được thực hành bằng Python
"""

class Employee:
    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0.0):
        if not id.strip():
            raise ValueError("Mã nhân sự không được rỗng.")
        if not fullName.strip():
            raise ValueError("Họ tên không được rỗng.")
        if baseSalary < 0:
            raise ValueError("Lương cơ bản không được âm.")
        self.id = id
        self.fullName = fullName
        self.baseSalary = float(baseSalary)

    # Mô phỏng overload: increaseSalary(amount) / increaseSalary(value, byPercentage)
    def increaseSalary(self, value, byPercentage=False):
        if value <= 0:
            raise ValueError("Giá trị tăng phải dương.")
        if byPercentage:
            self.baseSalary += self.baseSalary * value / 100
        else:
            self.baseSalary += value

    def calculateMonthlyCost(self):
        return self.baseSalary

    def displayInfo(self):
        print(f"ID: {self.id} | Họ tên: {self.fullName} | Lương cơ bản: {self.baseSalary:,.0f}")


class SoftwareEngineer(Employee):
    # Mô phỏng 2 constructor bằng tham số mặc định.
    def __init__(self, id, fullName, baseSalary_or_language,
                 primaryLanguage=None, technicalAllowance=0.0):
        if primaryLanguage is None:
            baseSalary = 0.0
            language = baseSalary_or_language
        else:
            baseSalary = baseSalary_or_language
            language = primaryLanguage

        if not str(language).strip():
            raise ValueError("Ngôn ngữ chính không được rỗng.")
        if technicalAllowance < 0:
            raise ValueError("Phụ cấp kỹ thuật không được âm.")

        super().__init__(id, fullName, baseSalary)
        self.primaryLanguage = language
        self.technicalAllowance = float(technicalAllowance)

    def calculateMonthlyCost(self):
        return self.baseSalary + self.technicalAllowance

    def displayInfo(self):
        print(f"ID: {self.id} | Họ tên: {self.fullName} | Lương cơ bản: {self.baseSalary:,.0f} | Ngôn ngữ: {self.primaryLanguage} | Phụ cấp: {self.technicalAllowance:,.0f}")


class ProjectTeam:
    def __init__(self, projectCode, projectName, leader=None):
        if not projectCode.strip():
            raise ValueError("Mã dự án không được rỗng.")
        if not projectName.strip():
            raise ValueError("Tên dự án không được rỗng.")
        self.projectCode = projectCode
        self.projectName = projectName
        self.leader = None
        self.members = []
        if leader is not None:
            self.leader = leader
            self.members.append(leader)

    # Mô phỏng overload: addMember(employee) / addMember(employee, makeLeader)
    def addMember(self, employee, makeLeader=False):
        if self.contains(employee.id):
            return False
        self.members.append(employee)
        if makeLeader:
            self.leader = employee
        return True

    def removeMember(self, employeeId):
        if self.leader is not None and self.leader.id == employeeId:
            return False
        for employee in self.members:
            if employee.id == employeeId:
                self.members.remove(employee)
                return True
        return False

    def changeLeader(self, employee):
        if not self.contains(employee.id):
            self.members.append(employee)
        self.leader = employee
        return True

    def contains(self, employeeId):
        return any(employee.id == employeeId for employee in self.members)

    def calculateTotalMonthlyCost(self):
        return sum(employee.calculateMonthlyCost() for employee in self.members)

    def displayTeam(self):
        print("\n" + "=" * 65)
        print(f"DỰ ÁN: {self.projectCode} - {self.projectName}")
        print("=" * 65)
        if self.leader is None:
            print("Trưởng nhóm: Chưa có")
        else:
            print(f"Trưởng nhóm: {self.leader.fullName} ({self.leader.id})")
        print("Danh sách thành viên:")
        if not self.members:
            print("  Chưa có thành viên.")
        else:
            for employee in self.members:
                employee.displayInfo()  # Đa hình
        print(f"Tổng chi phí nhân sự/tháng: {self.calculateTotalMonthlyCost():,.0f}")


def input_positive_float(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Giá trị phải lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")


def input_non_negative_float(message):
    while True:
        try:
            value = float(input(message))
            if value >= 0:
                return value
            print("Giá trị không được âm.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")


def input_employee():
    print("\n--- NHẬP EMPLOYEE ---")
    while True:
        employee_id = input("Mã nhân sự: ").strip()
        if employee_id:
            break
        print("Mã nhân sự không được rỗng.")
    while True:
        full_name = input("Họ tên: ").strip()
        if full_name:
            break
        print("Họ tên không được rỗng.")
    salary = input_non_negative_float("Lương cơ bản: ")
    return Employee(employee_id, full_name, salary)


def input_software_engineer():
    print("\n--- NHẬP SOFTWARE ENGINEER ---")
    while True:
        employee_id = input("Mã nhân sự: ").strip()
        if employee_id:
            break
        print("Mã nhân sự không được rỗng.")
    while True:
        full_name = input("Họ tên: ").strip()
        if full_name:
            break
        print("Họ tên không được rỗng.")
    salary = input_non_negative_float("Lương cơ bản: ")
    while True:
        language = input("Ngôn ngữ lập trình chính: ").strip()
        if language:
            break
        print("Ngôn ngữ không được rỗng.")
    allowance = input_non_negative_float("Phụ cấp kỹ thuật: ")
    return SoftwareEngineer(employee_id, full_name, salary, language, allowance)


def find_employee(employees, employee_id):
    for employee in employees:
        if employee.id == employee_id:
            return employee
    return None


def show_all_employees(employees):
    print("\n--- DANH SÁCH NHÂN SỰ ---")
    if not employees:
        print("Chưa có nhân sự.")
        return
    for employee in employees:
        employee.displayInfo()


def choose_team(teams):
    if not teams:
        print("Chưa có nhóm dự án.")
        return None
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team.projectCode} - {team.projectName}")
    try:
        index = int(input("Chọn nhóm: ")) - 1
        return teams[index]
    except (ValueError, IndexError):
        print("Nhóm không hợp lệ.")
        return None


def main():
    employees = []
    teams = []

    while True:
        print("\n" + "=" * 65)
        print("QUẢN LÝ NHÂN SỰ VÀ NHÓM DỰ ÁN")
        print("=" * 65)
        print("1. Thêm Employee")
        print("2. Thêm SoftwareEngineer")
        print("3. Hiển thị tất cả nhân sự")
        print("4. Tăng lương")
        print("5. Tạo ProjectTeam")
        print("6. Thêm nhân sự vào nhóm")
        print("7. Đặt/đổi trưởng nhóm")
        print("8. Xóa nhân sự khỏi nhóm")
        print("9. Hiển thị nhóm")
        print("10. Tính tổng chi phí nhóm")
        print("11. Xóa nhóm dự án")
        print("0. Thoát")
        choice = input("\nChọn chức năng: ").strip()

        try:
            if choice == "1":
                employee = input_employee()
                if find_employee(employees, employee.id):
                    print("Mã nhân sự đã tồn tại.")
                else:
                    employees.append(employee)
                    print("Đã thêm Employee thành công.")

            elif choice == "2":
                employee = input_software_engineer()
                if find_employee(employees, employee.id):
                    print("Mã nhân sự đã tồn tại.")
                else:
                    employees.append(employee)
                    print("Đã thêm SoftwareEngineer thành công.")

            elif choice == "3":
                show_all_employees(employees)

            elif choice == "4":
                if not employees:
                    print("Chưa có nhân sự.")
                    continue
                show_all_employees(employees)
                employee = find_employee(employees, input("Nhập mã nhân sự cần tăng lương: "))
                if employee is None:
                    print("Không tìm thấy nhân sự.")
                    continue
                print("1. Tăng theo số tiền cố định")
                print("2. Tăng theo phần trăm")
                mode = input("Chọn cách tăng: ")
                if mode == "1":
                    employee.increaseSalary(input_positive_float("Số tiền tăng: "))
                    print("Tăng lương thành công.")
                elif mode == "2":
                    employee.increaseSalary(input_positive_float("Phần trăm tăng: "), True)
                    print("Tăng lương thành công.")
                else:
                    print("Lựa chọn không hợp lệ.")

            elif choice == "5":
                code = input("Mã dự án: ").strip()
                name = input("Tên dự án: ").strip()
                teams.append(ProjectTeam(code, name))
                print("Tạo nhóm dự án thành công.")

            elif choice == "6":
                team = choose_team(teams)
                if team is None:
                    continue
                if not employees:
                    print("Chưa có nhân sự.")
                    continue
                show_all_employees(employees)
                employee = find_employee(employees, input("Nhập mã nhân sự cần thêm: "))
                if employee is None:
                    print("Không tìm thấy nhân sự.")
                    continue
                make_leader = input("Đặt làm trưởng nhóm? (y/n): ").lower() == "y"
                if team.addMember(employee, make_leader):
                    print("Thêm nhân sự thành công.")
                    if make_leader:
                        print("Nhân sự đã trở thành trưởng nhóm.")
                else:
                    print("Không thể thêm: nhân sự đã tồn tại trong nhóm.")

            elif choice == "7":
                team = choose_team(teams)
                if team is None:
                    continue
                show_all_employees(employees)
                employee = find_employee(employees, input("Nhập mã trưởng nhóm mới: "))
                if employee is None:
                    print("Không tìm thấy nhân sự.")
                    continue
                team.changeLeader(employee)
                print("Đổi trưởng nhóm thành công.")

            elif choice == "8":
                team = choose_team(teams)
                if team is None:
                    continue
                employee_id = input("Nhập mã nhân sự cần xóa: ")
                if team.removeMember(employee_id):
                    print("Xóa nhân sự thành công.")
                elif team.leader is not None and team.leader.id == employee_id:
                    print("Không thể xóa trưởng nhóm hiện tại. Hãy đổi trưởng nhóm trước.")
                else:
                    print("Không tìm thấy nhân sự trong nhóm.")

            elif choice == "9":
                if not teams:
                    print("Chưa có nhóm dự án.")
                    continue
                for team in teams:
                    team.displayTeam()

            elif choice == "10":
                team = choose_team(teams)
                if team is not None:
                    print(f"Tổng chi phí/tháng: {team.calculateTotalMonthlyCost():,.0f}")
            elif choice == "11":
                delete_team(teams, employees)
            elif choice == "0":
                print("\nKẾT THÚC CHƯƠNG TRÌNH.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as error:
            print(f"Lỗi: {error}")
def delete_team(teams, employees):
    if not teams:
        print("Chưa có nhóm dự án nào để xóa.")
        return
    # Chọn nhóm muốn xóa
    team_to_delete = choose_team(teams)
    if team_to_delete is None:
        return

    code = team_to_delete.projectCode
    name = team_to_delete.projectName

    # Xóa nhóm khỏi danh sách các nhóm
    teams.remove(team_to_delete)
    print(f"\n[TC 14] Đã xóa hoàn toàn nhóm dự án: {code} - {name}")

if __name__ == "__main__":
    main()
