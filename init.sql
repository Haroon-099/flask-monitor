

CREATE DATABASE IF NOT EXISTS statistics_db;


CREATE TABLE IF NOT EXISTS statistics_db.statistics(
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  disk_total BIGINT  NOT NULL,
  disk_used BIGINT  NOT NULL,
  disk_free BIGINT  NOT NULL,
  memory_total BIGINT  NOT NULL,
  memory_used BIGINT  NOT NULL,
  memory_free BIGINT  NOT NULL,
  cpu FLOAT NOT NULL,
  time  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO statistics_db.statistics (id, disk_total, disk_used, disk_free, memory_total, memory_used, memory_free, cpu, time)
VALUES
    (1, 51283869696, 34942267392, 16341602304, 8071704576, 1992761344, 5672112128, 2.1, '2024-01-28 16:32:00'),
    (2, 51283869696, 36791128064, 14492741632, 8071696384, 967438336, 6810112000, 2.1, '2024-01-28 16:38:39'),
    (3, 51283869696, 36839931904, 14443937792, 8071696384, 997679104, 6775074816, 2.6, '2024-01-28 16:41:51'),
    (4, 51283869696, 36839936000, 14443933696, 8071696384, 974852096, 6796996608, 1.6, '2024-01-28 16:45:37'),
    (5, 51283869696, 36839985152, 14443884544, 8071696384, 975695872, 6796070912, 2.1, '2024-01-28 16:47:02'),
    (6, 51283869696, 36840017920, 14443851776, 8071696384, 998559744, 6773043200, 2.6, '2024-01-28 16:48:02'),
    (7, 51283869696, 36839985152, 14443884544, 8071696384, 975515648, 6796156928, 1.6, '2024-01-28 16:49:02'),
    (8, 51283869696, 36840022016, 14443847680, 8071696384, 991879168, 6779625472, 2.1, '2024-01-28 16:50:02'),
    (9, 51283869696, 36839989248, 14443880448, 8071696384, 967761920, 6803775488, 1.6, '2024-01-28 16:51:02'),
    (10, 51283869696, 36840042496, 14443827200, 8071696384, 991510528, 6771482624, 2.1, '2024-01-28 16:52:01'),
    (11, 51283869696, 36839989248, 14443880448, 8071696384, 964571136, 6798487552, 2.1, '2024-01-28 16:53:01'),
    (12, 51283869696, 36840026112, 14443843584, 8071696384, 988508160, 6774472704, 2.1, '2024-01-28 16:54:01'),
    (13, 51283869696, 36839993344, 14443876352, 8071696384, 964546560, 6798483456, 1, '2024-01-28 16:55:02'),
    (14, 51283869696, 36840284160, 14443585536, 8071696384, 987897856, 6775050240, 1.6, '2024-01-28 16:56:02'),
    (15, 51283869696, 36840255488, 14443614208, 8071696384, 966356992, 6796652544, 2.6, '2024-01-28 16:57:02'),
    (16, 51283869696, 36840235008, 14443634688, 8071696384, 966160384, 6796836864, 0.5, '2024-01-28 16:58:02'),
    (17, 51283869696, 36840275968, 14443593728, 8071696384, 966221824, 6796783616, 2.1, '2024-01-28 16:59:01'),
    (18, 51283869696, 36840255488, 14443614208, 8071696384, 966172672, 6796828672, 2.1, '2024-01-28 17:00:01'),
    (19, 51283869696, 36840259584, 14443610112, 8071696384, 966270976, 6796734464, 2.1, '2024-01-28 17:01:01'),
    (20, 51283869696, 37013970944, 14269898752, 8071696384, 960540672, 6799732736, 3.2, '2024-01-28 17:23:46');

