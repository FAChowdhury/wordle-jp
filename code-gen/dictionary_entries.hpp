#pragma once
#include <array>
#include <cstdint>

#include "dictionary_constants.hpp"

namespace dictionary {
    struct RadicalRange {
        std::uint32_t offset;
        std::uint16_t count;
    };

    struct Entry {
        char32_t kanji;
        RadicalRange radicals;
    };

    inline constexpr std::array<Entry, KANJI_COUNT> entries {
        { U'左', { 0, 2 } },
        { U'右', { 2, 2 } },
        { U'友', { 4, 2 } },
        { U'気', { 6, 2 } },
        { U'六', { 8, 2 } },
        { U'休', { 10, 2 } },
        { U'才', { 12, 3 } },
        { U'分', { 15, 2 } },
        { U'何', { 17, 2 } },
        { U'谷', { 19, 3 } },
        { U'朝', { 22, 3 } },
        { U'安', { 25, 2 } },
        { U'妹', { 27, 2 } },
        { U'札', { 29, 2 } },
        { U'四', { 31, 2 } },
        { U'礼', { 33, 2 } },
        { U'花', { 35, 3 } },
        { U'菜', { 38, 3 } },
        { U'妥', { 41, 2 } },
        { U'好', { 43, 2 } },
        { U'町', { 45, 2 } },
        { U'猫', { 47, 3 } },
        { U'俺', { 50, 4 } },
        { U'孔', { 54, 2 } },
        { U'茶', { 56, 3 } }
    };
};
