from pick import pick

def SelectAllergy(FoodName:str, FoodIngredients:str)->dict:
    title = f'{FoodName} 알레르기 유발물질을 골라주세요\n{FoodIngredients}'
    options = ["우유", "메밀", "땅콩", "대두", "밀", "고등어", "게", "새우", "돼지고기", "복숭아", "토마토", "아황산류", "호두", "닭고기", "쇠고기", "오징어", "조개류", "달걀"]
    selected:list[tuple[str, int]] = pick(options, title, multiselect=True, min_selection_count=0)
    return {"food_name":FoodName.replace("\n",""), "allergy":[i[0] for i in selected]}

if __name__ == "__main__":
    print(SelectAllergy("HELLO"))