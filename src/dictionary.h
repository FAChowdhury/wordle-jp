# pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <span>

namespace dictionary {
	struct RadicalRange {
		std::uint32_t offset;
		std::uint16_t count;
	};

	struct Entry {
		char32_t kanji;
		RadicalRange radicals;
	};

	class Dictionary final {
	public:
		Dictionary() = delete;

		[[nodiscard]]
		static constexpr bool Contains(char32_t kanji);

		[[nodiscard]]
		static constexpr std::span<const char32_t> GetRadicals(char32_t kanji);

	private:
		static constexpr std::size_t KANJI_COUNT{};
		static constexpr std::size_t RADICAL_COUNT{};

		static constexpr std::array<Entry, KANJI_COUNT> entries;
		static constexpr std::array<char32_t, RADICAL_COUNT> radicals;
	};

};
