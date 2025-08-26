# import-as, from-import 구문 사용
# 1.1 our_class_pkg 패키지의 ofiicial 패키지의 official_module을 om 별칭으로 가져오고
# 1-2. our_class_pkg 패키지의 unofficial 패키지의 unofficial_module을 from-import 로 가져와주세요.

import our_class_pkg.official.official_module as om
from our_class_pkg.unofficial.unofficial_module import study, lecture
