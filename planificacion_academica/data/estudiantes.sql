INSERT INTO estudiante ("idestudiante", "uc1", "uc2", "uc3", "uc4", "uc5", "uc6", "uc7", "uc8", "uc9", "uc10", "uc11", "uc12", "uc13", "uc14", "uc15", "uc16", "uc17", "uc18", "uc19")
SELECT 1, 0, 1, 1, 1, 1, 2, 0, 0, 2, 1, 2, 0, 0, 1, 0, 0, 1, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 1
)
UNION ALL SELECT 2, 0, 2, 0, 0, 0, 0, 2, 2, 1, 1, 0, 2, 2, 0, 1, 0, 1, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 2
)
UNION ALL SELECT 3, 0, 2, 2, 2, 0, 1, 1, 1, 2, 0, 1, 0, 1, 2, 0, 0, 2, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 3
)
UNION ALL SELECT 4, 0, 2, 2, 1, 0, 2, 0, 1, 2, 0, 2, 1, 2, 2, 2, 0, 1, 0, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 4
)
UNION ALL SELECT 5, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 2, 0, 0, 2, 1, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 5
)
UNION ALL SELECT 6, 2, 2, 1, 0, 0, 1, 2, 2, 0, 2, 0, 2, 2, 1, 1, 2, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 6
)
UNION ALL SELECT 7, 0, 0, 0, 1, 1, 1, 2, 1, 0, 0, 1, 0, 1, 2, 2, 0, 1, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 7
)
UNION ALL SELECT 8, 1, 2, 1, 2, 1, 1, 2, 2, 0, 1, 2, 1, 1, 2, 0, 1, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 8
)
UNION ALL SELECT 9, 1, 2, 2, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 9
)
UNION ALL SELECT 10, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 2, 2, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 10
)
UNION ALL SELECT 11, 1, 1, 1, 1, 2, 1, 1, 0, 2, 1, 1, 0, 0, 2, 1, 1, 2, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 11
)
UNION ALL SELECT 12, 2, 2, 0, 2, 0, 1, 2, 2, 1, 0, 0, 1, 2, 1, 2, 0, 2, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 12
)
UNION ALL SELECT 13, 2, 2, 1, 1, 2, 0, 2, 2, 2, 0, 2, 0, 1, 0, 2, 1, 1, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 13
)
UNION ALL SELECT 14, 1, 2, 2, 1, 1, 0, 2, 1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 14
)
UNION ALL SELECT 15, 2, 0, 0, 0, 1, 1, 0, 1, 0, 2, 1, 1, 2, 0, 0, 1, 0, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 15
)
UNION ALL SELECT 16, 1, 2, 0, 2, 1, 1, 0, 0, 0, 1, 2, 1, 1, 2, 2, 1, 0, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 16
)
UNION ALL SELECT 17, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2, 1, 0, 2, 0, 1, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 17
)
UNION ALL SELECT 18, 1, 1, 1, 2, 1, 1, 2, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 18
)
UNION ALL SELECT 19, 0, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 0, 1, 0, 0, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 19
)
UNION ALL SELECT 20, 1, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 20
)
UNION ALL SELECT 21, 1, 1, 2, 1, 0, 0, 2, 1, 2, 0, 2, 0, 1, 0, 1, 1, 2, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 21
)
UNION ALL SELECT 22, 0, 2, 2, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 2, 0, 2, 1, 0, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 22
)
UNION ALL SELECT 23, 1, 1, 1, 2, 0, 0, 0, 1, 1, 0, 0, 1, 2, 1, 2, 1, 2, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 23
)
UNION ALL SELECT 24, 0, 1, 1, 1, 0, 2, 0, 2, 2, 2, 0, 1, 2, 1, 0, 1, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 24
)
UNION ALL SELECT 25, 0, 2, 0, 1, 0, 0, 2, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 25
)
UNION ALL SELECT 26, 0, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 26
)
UNION ALL SELECT 27, 1, 0, 2, 0, 2, 0, 0, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 27
)
UNION ALL SELECT 28, 0, 1, 1, 0, 2, 1, 0, 2, 2, 0, 1, 1, 0, 2, 2, 1, 2, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 28
)
UNION ALL SELECT 29, 2, 2, 1, 0, 2, 0, 0, 1, 2, 2, 2, 1, 1, 0, 0, 0, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 29
)
UNION ALL SELECT 30, 1, 1, 1, 2, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 30
)
UNION ALL SELECT 31, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 2, 1, 2, 2, 0, 1, 2, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 31
)
UNION ALL SELECT 32, 1, 1, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 0, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 32
)
UNION ALL SELECT 33, 1, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 2, 0, 1, 2, 0, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 33
)
UNION ALL SELECT 34, 2, 0, 0, 1, 1, 0, 2, 2, 0, 1, 2, 2, 2, 1, 2, 2, 0, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 34
)
UNION ALL SELECT 35, 1, 1, 2, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 35
)
UNION ALL SELECT 36, 2, 0, 2, 2, 1, 1, 1, 2, 1, 1, 0, 0, 2, 0, 0, 2, 2, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 36
)
UNION ALL SELECT 37, 2, 1, 2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 1, 0, 2, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 37
)
UNION ALL SELECT 1, 0, 1, 1, 1, 1, 2, 0, 0, 2, 1, 2, 0, 0, 1, 0, 0, 1, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 1
)
UNION ALL SELECT 38,0,0,1,1,0,1,1,2,1,0,0,2,1,1,2,2,1,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 38
)
UNION ALL SELECT 39,1,2,0,0,0,2,2,2,2,2,0,1,0,1,1,1,1,0,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 39
)
UNION ALL SELECT 40,0,1,1,2,0,0,2,2,2,1,2,0,1,1,1,2,2,2,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 40
)
UNION ALL SELECT 41,2,1,2,2,1,2,0,2,1,1,2,0,0,2,0,1,1,1,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 41
)
UNION ALL SELECT 42,2,1,0,2,2,2,0,2,0,2,0,0,1,1,1,1,2,0,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 42
)
UNION ALL SELECT 43,0,1,0,1,2,0,1,0,0,0,2,2,2,1,0,2,2,0,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 43
)
UNION ALL SELECT 44,0,0,2,0,0,1,1,0,1,1,2,0,1,1,1,1,0,0,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 44
)
UNION ALL SELECT 45,0,2,0,1,0,2,0,1,2,0,0,0,0,0,0,1,2,1,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 45
)
UNION ALL SELECT 46,2,1,1,2,1,0,0,0,2,1,1,2,2,2,0,2,0,2,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 46
)
UNION ALL SELECT 47,2,0,2,0,2,2,2,2,0,0,1,0,0,1,0,2,1,1,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 47
)
UNION ALL SELECT 48,2,2,1,0,0,0,0,2,1,1,2,0,0,2,2,2,1,1,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 48
)
UNION ALL SELECT 49,1,1,0,1,1,0,2,0,0,2,2,1,0,0,1,0,1,1,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 49
)
UNION ALL SELECT 50, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 50
)
UNION ALL SELECT 51, 1, 2, 2, 0, 0, 0, 2, 0, 1, 2, 1, 0, 0, 1, 2, 2, 2, 2, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 51
)
UNION ALL SELECT 52, 2, 2, 0, 1, 1, 1, 0, 2, 1, 1, 0, 1, 0, 0, 1, 1, 2, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 52
)
UNION ALL SELECT 53, 2, 1, 2, 2, 0, 0, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 2, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 53
)
UNION ALL SELECT 54, 0, 0, 1, 0, 2, 0, 0, 2, 2, 2, 1, 1, 2, 2, 1, 0, 0, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 54
)
UNION ALL SELECT 55, 1, 1, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 2, 0, 2, 0, 2, 0, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 55
)
UNION ALL SELECT 56, 1, 1, 0, 1, 1, 2, 1, 2, 2, 0, 0, 2, 2, 2, 2, 1, 1, 0, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 56
)
UNION ALL SELECT 57, 2, 1, 1, 0, 0, 2, 2, 0, 2, 1, 0, 0, 0, 0, 2, 0, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 57
)
UNION ALL SELECT 58, 2, 0, 1, 0, 1, 1, 0, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 58
)
UNION ALL SELECT 59, 1, 0, 1, 0, 1, 2, 2, 1, 1, 0, 2, 2, 1, 0, 2, 1, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 59
)
UNION ALL SELECT 60, 0, 2, 2, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 60
)
UNION ALL SELECT 61, 0, 0, 0, 0, 2, 1, 0, 1, 2, 0, 1, 0, 0, 1, 2, 1, 2, 2, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 61
)
UNION ALL SELECT 1, 0, 1, 1, 1, 1, 2, 0, 0, 2, 1, 2, 0, 0, 1, 0, 0, 1, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 1
)
UNION ALL SELECT 62, 0, 1, 0, 2, 0, 2, 0, 2, 1, 0, 1, 0, 0, 2, 2, 0, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 62
)
UNION ALL SELECT 63, 2, 0, 2, 0, 0, 2, 2, 1, 1, 0, 2, 2, 0, 2, 2, 1, 2, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 63
)
UNION ALL SELECT 64, 0, 0, 2, 0, 2, 0, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 2, 0, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 64
)
UNION ALL SELECT 65, 2, 1, 0, 1, 2, 0, 0, 1, 0, 2, 2, 0, 0, 0, 1, 2, 1, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 65
)
UNION ALL SELECT 66, 1, 1, 2, 0, 0, 2, 2, 1, 1, 2, 2, 1, 2, 0, 2, 1, 0, 1, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 66
)
UNION ALL SELECT 67, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 67
)
UNION ALL SELECT 68, 1, 2, 0, 2, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 2, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 68
)
UNION ALL SELECT 69, 1, 2, 1, 1, 2, 0, 2, 0, 2, 1, 1, 0, 1, 0, 2, 2, 1, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 69
)
UNION ALL SELECT 70, 2, 2, 0, 1, 2, 2, 0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 70
)
UNION ALL SELECT 71, 1, 1, 0, 0, 2, 1, 1, 0, 0, 2, 1, 2, 2, 0, 2, 2, 2, 2, 1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 71
)
UNION ALL SELECT 72, 0, 0, 1, 1, 1, 2, 2, 1, 2, 1, 0, 2, 2, 0, 1, 0, 0, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 72
)
UNION ALL SELECT 73, 2, 0, 2, 1, 0, 1, 0, 1, 1, 1, 0, 0, 2, 0, 1, 0, 1, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 73
)
UNION ALL SELECT 74, 2, 2, 1, 1, 1, 0, 2, 0, 2, 1, 1, 0, 2, 0, 0, 1, 0, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 74
)
UNION ALL SELECT 75, 1, 2, 1, 2, 0, 0, 0, 1, 2, 2, 2, 1, 0, 2, 2, 0, 0, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 75
)
UNION ALL SELECT 76, 0, 2, 1, 2, 0, 0, 1, 2, 1, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 76
)
UNION ALL SELECT 77, 1, 0, 1, 1, 1, 0, 1, 2, 2, 0, 0, 1, 2, 2, 0, 1, 0, 1, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 77
)
UNION ALL SELECT 78, 2, 2, 1, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 2, 0, 2, 2, 0, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 78
)
UNION ALL SELECT 79, 2, 0, 2, 0, 0, 2, 1, 0, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 79
)
UNION ALL SELECT 80, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 80
)
UNION ALL SELECT 81,0,1,1,1,1,1,2,0,0,1,2,2,0,1,0,2,1,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 81
)
UNION ALL SELECT 82,1,1,0,0,2,2,1,2,0,0,0,0,2,1,1,0,0,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 82
)
UNION ALL SELECT 83,1,0,2,0,0,0,2,2,2,0,1,0,0,0,1,2,2,0,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 83
)
UNION ALL SELECT 84,0,1,0,2,1,1,1,2,0,2,1,1,0,0,0,1,1,0,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 84
)
UNION ALL SELECT 85,0,0,0,2,1,0,1,0,2,2,2,1,1,1,2,1,0,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 85
)
UNION ALL SELECT 86,1,1,0,1,1,1,2,2,0,0,1,2,1,1,2,0,2,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 86
)
UNION ALL SELECT 87,1,2,0,1,2,1,1,1,0,2,0,0,0,2,1,1,0,0,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 87
)
UNION ALL SELECT 88,1,1,2,1,1,2,0,0,0,0,0,1,2,0,1,0,1,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 88
)
UNION ALL SELECT 89,0,1,2,0,0,0,0,1,1,1,0,0,2,2,0,2,1,2,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 89
)
UNION ALL SELECT 90,2,1,2,2,1,2,1,1,2,2,2,2,2,0,2,0,1,0,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 90
)
UNION ALL SELECT 91,1,2,1,0,1,2,0,2,0,0,0,2,1,1,0,0,0,1,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 91
)
UNION ALL SELECT 92,1,0,0,2,1,1,0,2,2,2,0,0,2,1,2,0,1,0,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 92
)
UNION ALL SELECT 93,0,2,0,1,0,0,0,0,0,2,1,1,0,0,1,0,2,1,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 93
)
UNION ALL SELECT 94,1,0,0,1,0,2,0,1,2,1,0,1,1,0,0,0,2,0,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 94
)
UNION ALL SELECT 95,1,0,1,0,0,0,0,2,0,1,0,1,0,2,1,0,0,2,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 95
)
UNION ALL SELECT 96,0,1,0,0,2,0,2,1,1,0,1,0,0,1,2,2,0,1,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 96
)
UNION ALL SELECT 97,1,2,1,2,2,1,2,1,2,1,0,2,2,1,2,2,0,0,2
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 97
)
UNION ALL SELECT 98,2,1,1,0,1,1,0,0,2,1,1,2,2,1,0,2,2,0,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 98
)
UNION ALL SELECT 99,1,1,2,1,0,0,0,0,0,2,1,1,2,0,0,2,2,2,0
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 99
)
UNION ALL SELECT 100,1,2,1,1,0,1,2,2,1,1,1,2,0,0,2,1,2,2,1
WHERE NOT EXISTS (
  SELECT 1 FROM estudiante WHERE "idestudiante" = 100
);